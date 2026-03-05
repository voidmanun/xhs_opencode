"""
consumer.py - 消息消费者
每 5 秒扫描 SQLite 中 pending 状态的消息，执行处理逻辑
"""
import time
import json
import logging
import subprocess
import os
from pathlib import Path

from message_store import init_db, fetch_pending, update_status, get_stats

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [Consumer] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent / "consumer.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

CONSUME_INTERVAL = 5    # 消费轮询间隔（秒）
BATCH_SIZE = 10          # 每次消费批量大小

# reply.sh 脚本路径
REPLY_SCRIPT = Path(__file__).parent / "doc" / "reply.sh"


def handle_message(msg: dict) -> bool:
    """
    处理单条消息的业务逻辑：
    1. 调用 opencode agent 生成回复内容
    2. 调用 reply.sh 将回复发送到小红书

    Args:
        msg: 消息字典，包含 comment_content, user_nickname, note_content 等字段

    Returns:
        True 表示处理并回复成功，False 表示失败
    """
    msg_type = msg.get("type", "")
    user = msg.get("user_nickname", "未知用户")
    comment = msg.get("comment_content", "")
    note = msg.get("note_content", "")
    note_id = msg.get("note_id", "")
    comment_id = msg.get("comment_id", "")
    xsec_token = msg.get("xsec_token", "")  # Add xsec_token

    # 对于回复类型的消息，需要把回复挂到被回复的那条评论下而不是新评论上
    if msg_type == "comment/comment":
        target = msg.get("target_comment_content", "")
        # 从 raw_json 中提取真正的 target_comment.id
        try:
            raw_msg = json.loads(msg.get("raw_json", "{}"))
            target_comment_id = raw_msg.get("comment_info", {}).get("target_comment", {}).get("id", comment_id)
            if target_comment_id:
                comment_id = target_comment_id
        except:
            pass
            
        logger.info(
            f"💬 处理回复消息: {user} 回复了 \"{target[:30]}...\" → \"{comment}\""
        )
    else:
        logger.info(
            f"💬 处理评论消息: {user} 在笔记 \"{note[:20]}...\" 评论: \"{comment}\""
        )

    # === 第零步：发送初始确认回复 ===
    try:
        ack_msg = "收到，马上为您安排。"
        logger.info(f"📤 正在发送初始确认回复: content='{ack_msg}'")
        # 修改为调用 doc/reply.py
        reply_script_py = str(Path(__file__).parent / "doc" / "reply.py")
        ack_result = subprocess.run(
            ["python3", reply_script_py, note_id, comment_id, ack_msg, xsec_token],
            capture_output=True,
            text=True,
            check=False
        )
        if ack_result.returncode == 0:
            logger.info(f"✅ 初始确认回复发出，响应返回码 0。输出内容:\n{ack_result.stdout.strip()}\n{ack_result.stderr.strip()}")
        else:
            logger.warning(f"⚠️ 初始确认回复失败 (code {ack_result.returncode})，将继续执行 agent 发送。\n错误信息:\n{ack_result.stderr.strip()}")
    except Exception as e:
        logger.warning(f"⚠️ 调用初始 reply.py 时发生错误: {e}")

    # === 第一步：调用 opencode --agent gamemaker 生成回复 ===
    try:
        logger.info(f"🚀 正在发送消息给 gamemaker agent: '{comment}'")
        # 修改为使用 opencode 的绝对路径，并移除对 /bin/zsh 的硬依赖
        opencode_path = "/root/.opencode/bin/opencode"
        if not os.path.exists(opencode_path):
            opencode_path = "opencode"  # fallback
            
        cmd_str = f"{opencode_path} run --agent gamemaker '{comment}'"
        result = subprocess.run(
            cmd_str,
            shell=True,
            capture_output=True,
            text=True,
            check=False,
            cwd="/root/workspace/share_game"
        )

        if result.returncode != 0:
            logger.error(f"❌ gamemaker 处理失败 (code {result.returncode})。\n错误信息:\n{result.stderr.strip()}")
            return False

        reply_content = result.stdout.strip()
        logger.info(f"✅ gamemaker 处理成功。返回结果:\n{reply_content}")

    except FileNotFoundError:
        logger.error("❌ 找不到 'opencode' 命令，请确保它已安装并在 PATH 中。")
        return False
    except Exception as e:
        logger.error(f"❌ 调用 opencode 时发生未知错误: {e}")
        return False

    # === 第二步：调用 reply.sh 回复评论 ===
    if not reply_content:
        logger.warning("⚠️ gamemaker 返回内容为空，跳过回复")
        return False

    try:
        logger.info(f"📤 正在回复评论: note_id={note_id}, comment_id={comment_id}, content='{reply_content[:50]}...'")
        reply_script_py = str(Path(__file__).parent / "doc" / "reply.py")
        reply_result = subprocess.run(
            ["python3", reply_script_py, note_id, comment_id, reply_content, xsec_token],
            capture_output=True,
            text=True,
            check=False
        )

        if reply_result.returncode == 0:
            logger.info(f"✅ 回复成功！响应:\n{reply_result.stdout.strip()}")
            return True
        else:
            logger.error(f"❌ 回复失败 (code {reply_result.returncode})。\n错误信息:\n{reply_result.stderr.strip()}")
            return False

    except Exception as e:
        logger.error(f"❌ 调用 reply.sh 时发生错误: {e}")
        return False


def consume_once():
    """执行一次消费：拉取 pending 消息 → 处理 → 更新状态"""
    messages = fetch_pending(limit=BATCH_SIZE)

    if not messages:
        return

    logger.info(f"📤 拉取到 {len(messages)} 条待处理消息")

    for msg in messages:
        msg_id = msg["id"]
        note_id = msg.get("note_id", "")
        comment_content = msg.get("comment_content", "")
        
        # 提取 xsec_token (针对 comment/comment 等情况)
        try:
            raw_msg = json.loads(msg["raw_json"])
            # 先尝试从顶层取，对于 note_info 可能在顶层
            token = raw_msg.get("item_info", {}).get("xsec_token", "")
            if not token:
                # 尝试从 comment_info 的外层或自身附带信息取
                token = raw_msg.get("user_info", {}).get("xsec_token", "")
            msg["xsec_token"] = token
            logger.info(f"🔑 提取到 xsec_token: '{token}' (msg_id: {msg_id})")
        except Exception as e:
            logger.error(f"❌ 提取 xsec_token 失败 (msg_id: {msg_id}): {e}")
            msg["xsec_token"] = ""
        
        # 只处理以"听我说"开头的评论，其他评论直接忽略
        if not comment_content.startswith("听我说"):
            logger.info(f"⏭️ 忽略非目标评论: {msg_id} (评论内容不以'听我说'开头: '{comment_content[:30]}...')")
            try:
                update_status(msg_id, "ignored")
            except Exception as e:
                logger.error(f"❌ 忽略消息 {msg_id} 失败: {e}")
            continue

        try:
            update_status(msg_id, "processing")
            success = handle_message(msg)
            if success:
                update_status(msg_id, "done")
            else:
                update_status(msg_id, "failed")
        except Exception as e:
            logger.error(f"❌ 处理消息 {msg_id} 失败: {e}")
            update_status(msg_id, "failed")

    stats = get_stats()
    logger.info(f"队列状态: {stats}")


def run():
    """启动 Consumer 消费循环"""
    logger.info("🚀 Consumer 启动，消费频率：每 %d 秒", CONSUME_INTERVAL)
    init_db()

    while True:
        consume_once()
        time.sleep(CONSUME_INTERVAL)


if __name__ == "__main__":
    run()
