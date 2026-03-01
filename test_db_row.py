import sqlite3, json, traceback
conn = sqlite3.connect("messages.db")
conn.row_factory = sqlite3.Row
row = conn.execute("SELECT * FROM messages WHERE id='7612189999941605918'").fetchone()
msg = dict(row)
try:
    raw_msg = json.loads(msg["raw_json"])
    token = raw_msg.get("item_info", {}).get("xsec_token", "")
    print("SUCCESS TOKEN:", token)
except Exception as e:
    traceback.print_exc()
