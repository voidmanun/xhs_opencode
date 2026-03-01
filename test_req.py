import json
import urllib.request
import urllib.parse
from pathlib import Path

AUTH_FILE = Path(__file__).parent / "doc" / "auth.json"

try:
    with open(AUTH_FILE, "r", encoding="utf-8") as f:
        auth_data = json.load(f)["reply"]
except Exception as e:
    print(f"Error loading auth: {e}")
    exit(1)

url = 'https://edith.xiaohongshu.com/api/sns/web/v1/comment/post'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': auth_data.get('cookie', ''),
    'origin': 'https://www.xiaohongshu.com',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-b3-traceid': auth_data.get('x_b3_traceid', ''),
    'x-s': auth_data.get('x_s', ''),
    'x-s-common': auth_data.get('x_s_common', ''),
    'x-t': auth_data.get('x_t', ''),
    'x-xray-traceid': auth_data.get('x_xray_traceid', '')
}

data = {
    "note_id": "69a3e092000000001a027ba6",
    "target_comment_id": "69a3f00c000000000f029078",
    "content": "Python 直连测试",
    "at_users": []
}

data_bytes = json.dumps(data, ensure_ascii=False).replace(" ", "").encode('utf-8')

req = urllib.request.Request(url, data=data_bytes, headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(f"Status Code: {response.getcode()}")
        print(f"Response: {result}")
except Exception as e:
    if hasattr(e, 'read'):
         print(f"Error Response: {e.read().decode('utf-8')}")
    print(f"Exception: {e}")
