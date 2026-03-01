"""
timer_producer.py - 定时生产者
每 60 秒调用 fetchMentions.sh 获取评论通知，将新消息写入 SQLite
"""
import time
import subprocess
import json
import logging
import os
from pathlib import Path

from message_store import init_db, insert_message, get_stats

# 切换到脚本所在目录，确保能正确调用 fetchMentions.sh
SCRIPT_DIR = Path(__file__).parent / "doc"

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [Producer] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent / "producer.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

POLL_INTERVAL = 60  # 轮询间隔（秒）


def fetch_mentions() -> dict | None:
    """调用 fetchMentions.sh 获取 JSON 数据"""
    try:
        result = subprocess.run(
            ["sh", str(SCRIPT_DIR / "fetchMentions.sh")],
            capture_output=True, text=True, check=True,
            cwd=str(SCRIPT_DIR)
        )
        output = result.stdout.strip()
        if not output:
            logger.warning("fetchMentions.sh 没有返回任何内容")
            return None

        # 解析 JSON，处理可能的额外输出
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            output = output[output.find('{'):output.rfind('}') + 1]
            return json.loads(output)

    except subprocess.CalledProcessError as e:
        logger.error(f"执行 fetchMentions.sh 失败: {e.stderr}")
    except json.JSONDecodeError as e:
        logger.error(f"JSON 解析失败: {e}")
    except Exception as e:
        logger.error(f"发生未知错误: {e}")
    return None


def produce_once():
    """执行一次生产：拉取评论 → 写入数据库"""
    data = fetch_mentions()
    if data is None:
        return

    if not data.get("success"):
        logger.error(f"接口返回失败: {data.get('msg', '未知错误')}")
        return

    message_list = data.get("data", {}).get("message_list", [])
    new_count = 0

    for msg in message_list:
        if insert_message(msg):
            new_count += 1
            user_name = msg.get("user_info", {}).get("nickname", "未知")
            content = msg.get("comment_info", {}).get("content", "")
            logger.info(f"📥 新消息入库: {user_name} 说 \"{content}\"")

    stats = get_stats()
    logger.info(
        f"本次轮询: 获取 {len(message_list)} 条，新增 {new_count} 条 | "
        f"队列状态: {stats}"
    )


def run():
    """启动 Producer 定时循环"""
    logger.info("🚀 Producer 启动，轮询频率：每 %d 秒", POLL_INTERVAL)
    init_db()

    # 立即执行一次
    produce_once()

    # 定时循环
    while True:
        time.sleep(POLL_INTERVAL)
        produce_once()


if __name__ == "__main__":
    run()
