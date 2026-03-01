import json, traceback
msg = {"raw_json": '{"item_info": {"xsec_token": "LBgg"}}'}
try:
    raw_msg = json.loads(msg["raw_json"])
    token = raw_msg.get("item_info", {}).get("xsec_token", "")
    print("TOKEN:", token)
except Exception as e:
    traceback.print_exc()
