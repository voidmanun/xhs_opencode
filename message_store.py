"""
message_store.py - SQLite 消息存储层
负责建表、插入消息（去重）、查询待处理消息、更新状态
"""
import sqlite3
import json
import logging
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "messages.db"

logger = logging.getLogger(__name__)


def get_connection():
    """获取 SQLite 连接，启用 WAL 模式支持并发读写"""
    conn = sqlite3.connect(str(DB_PATH), timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn


def init_db():
    """初始化数据库表"""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id              TEXT PRIMARY KEY,
            type            TEXT,
            user_nickname   TEXT,
            user_id         TEXT,
            comment_content TEXT,
            comment_id      TEXT,
            note_id         TEXT,
            note_content    TEXT,
            target_comment_content TEXT,
            raw_json        TEXT,
            status          TEXT DEFAULT 'pending',
            created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
            processed_at    DATETIME
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_messages_status
        ON messages(status)
    """)
    conn.commit()
    conn.close()
    logger.info("数据库初始化完成")


def insert_message(msg: dict) -> bool:
    """
    插入一条消息，利用 INSERT OR IGNORE 做去重。
    返回 True 表示新插入，False 表示已存在。
    """
    msg_id = msg.get("id", "")
    msg_type = msg.get("type", "")
    user_info = msg.get("user_info", {})
    comment_info = msg.get("comment_info", {})
    item_info = msg.get("item_info", {})

    # 提取被回复的原评论内容（仅 comment/comment 类型）
    target_comment = comment_info.get("target_comment", {})
    target_content = target_comment.get("content", "") if target_comment else ""

    conn = get_connection()
    cursor = conn.execute("""
        INSERT OR IGNORE INTO messages
        (id, type, user_nickname, user_id, comment_content, comment_id,
         note_id, note_content, target_comment_content, raw_json, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending')
    """, (
        msg_id,
        msg_type,
        user_info.get("nickname", ""),
        user_info.get("userid", ""),
        comment_info.get("content", ""),
        comment_info.get("id", ""),
        item_info.get("id", ""),
        item_info.get("content", ""),
        target_content,
        json.dumps(msg, ensure_ascii=False),
    ))
    inserted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return inserted


def fetch_pending(limit: int = 10) -> list[dict]:
    """查询待处理消息"""
    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM messages
        WHERE status = 'pending'
        ORDER BY created_at ASC
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def update_status(msg_id: str, status: str):
    """更新消息状态：processing / done / failed / ignored"""
    conn = get_connection()
    processed_at = datetime.now().isoformat() if status in ("done", "failed", "ignored") else None
    conn.execute("""
        UPDATE messages
        SET status = ?, processed_at = ?
        WHERE id = ?
    """, (status, processed_at, msg_id))
    conn.commit()
    conn.close()


def get_stats() -> dict:
    """获取各状态消息统计"""
    conn = get_connection()
    rows = conn.execute("""
        SELECT status, COUNT(*) as cnt
        FROM messages
        GROUP BY status
    """).fetchall()
    conn.close()
    return {row["status"]: row["cnt"] for row in rows}
