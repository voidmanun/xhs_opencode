"""
consumer.py - 消息消费者
每 5 秒扫描 SQLite 中 pending 状态的消息，执行处理逻辑
"""
import time
import logging
import subprocess
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


def handle_message(msg: dict):
    """
    处理单条消息的业务逻辑。
    当前版本：日志输出。
    后续可替换为 Gemini 生图 / 自动回复等。

    Args:
        msg: 消息字典，包含 comment_content, user_nickname, note_content 等字段
    """
    msg_type = msg.get("type", "")
    user = msg.get("user_nickname", "未知用户")
    comment = msg.get("comment_content", "")
    note = msg.get("note_content", "")

    if msg_type == "comment/comment":
        target = msg.get("target_comment_content", "")
        logger.info(
            f"💬 处理回复消息: {user} 回复了 \"{target[:30]}...\" → \"{comment}\""
        )
    else:
        logger.info(
            f"💬 处理评论消息: {user} 在笔记 \"{note[:20]}...\" 评论: \"{comment}\""
        )

    # 调用 opencode --agent gamemaker 将评论发送过去
    try:
        logger.info(f"🚀 正在发送消息给 gamemaker agent: '{comment}'")
        # capture_output=True 获取标准输出和标准错误，text=True 表示以字符串形式返回
        result = subprocess.run(
            ["opencode", "run","--agent", "gamemaker", comment],
            capture_output=True,
            text=True,
            check=False  # 设置为 False 防止非 0 退出码抛出异常退出消费循环
        )
        
        # 记录执行结果
        if result.returncode == 0:
            logger.info(f"✅ gamemaker 处理成功。返回结果:\n{result.stdout.strip()}")
        else:
            logger.error(f"❌ gamemaker 处理失败 (code {result.returncode})。\n错误信息:\n{result.stderr.strip()}")
            
    except FileNotFoundError:
        logger.error("❌ 找不到 'opencode' 命令，请确保它已安装并在 PATH 中。")
    except Exception as e:
        logger.error(f"❌ 调用 opencode 时发生未知错误: {e}")


def consume_once():
    """执行一次消费：拉取 pending 消息 → 处理 → 更新状态"""
    messages = fetch_pending(limit=BATCH_SIZE)

    if not messages:
        return

    logger.info(f"📤 拉取到 {len(messages)} 条待处理消息")

    for msg in messages:
        msg_id = msg["id"]
        try:
            update_status(msg_id, "processing")
            handle_message(msg)
            update_status(msg_id, "done")
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
