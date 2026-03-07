"""
run.py - 一键启动入口
同时在多个线程中运行 Producer、Consumer 和 Dashboard
"""
import threading
import logging
import signal
import sys

from timer_producer import run as run_producer
from consumer import run as run_consumer
from dashboard import run_dashboard

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def signal_handler(sig, frame):
    """优雅退出"""
    logger.info("\n🛑 收到退出信号，正在关闭...")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("=" * 50)
    logger.info("🍌 小红书评论消息系统启动")
    logger.info("  Producer: 每 60 秒轮询 API → 写入消息")
    logger.info("  Consumer: 每 5 秒消费待处理消息")
    logger.info("  Dashboard: http://localhost:8080")
    logger.info("=" * 50)

    # Producer 线程
    producer_thread = threading.Thread(
        target=run_producer,
        name="Producer",
        daemon=True
    )

    # Consumer 线程
    consumer_thread = threading.Thread(
        target=run_consumer,
        name="Consumer",
        daemon=True
    )

    # Dashboard 线程
    dashboard_thread = threading.Thread(
        target=run_dashboard,
        kwargs={"port": 8080},
        name="Dashboard",
        daemon=True
    )
    
    producer_thread.start()
    consumer_thread.start()
    dashboard_thread.start()

    # 主线程等待（daemon 线程会随主线程退出）
    try:
        while True:
            producer_thread.join(timeout=1)
            consumer_thread.join(timeout=1)
            dashboard_thread.join(timeout=1)
    except (KeyboardInterrupt, SystemExit):
        logger.info("🛑 系统已关闭")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "manual":
        # 如果带有 manual 参数，启动手动测试入口
        import manual
        manual.main()
    else:
        main()
