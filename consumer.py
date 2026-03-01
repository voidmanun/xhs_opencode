"""
consumer.py - 消息消费者
每 5 秒扫描 SQLite 中 pending 状态的消息，执行处理逻辑
"""
import time
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

# 配置特定笔记的关键词（如果笔记内容包含该关键词，则处理该笔记下的回复）
TARGET_NOTE_KEYWORD = os.getenv("TARGET_NOTE_KEYWORD", "游戏共创") 


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

    if msg_type == "comment/comment":
        target = msg.get("target_comment_content", "")
        logger.info(
            f"💬 处理回复消息: {user} 回复了 \"{target[:30]}...\" → \"{comment}\""
        )
    else:
        logger.info(
            f"💬 处理评论消息: {user} 在笔记 \"{note[:20]}...\" 评论: \"{comment}\""
        )

    # === 第一步：调用 opencode --agent gamemaker 生成回复 ===
    try:
        logger.info(f"🚀 正在发送消息给 gamemaker agent: '{comment}'")
        result = subprocess.run(
            ["opencode", "run", "--agent", "gamemaker", comment],
            capture_output=True,
            text=True,
            check=False
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
        reply_result = subprocess.run(
            ["bash", str(REPLY_SCRIPT), note_id, comment_id, reply_content],
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
        note_content = msg.get("note_content", "")
        
        # 如果配置了特定的笔记关键词，且当前消息的笔记内容不包含该关键词，则直接置为 ignored
        if TARGET_NOTE_KEYWORD and TARGET_NOTE_KEYWORD not in note_content:
            logger.info(f"⏭️ 忽略非目标笔记的消息: {msg_id} (note_id: {note_id}, 未包含关键词 '{TARGET_NOTE_KEYWORD}')")
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
