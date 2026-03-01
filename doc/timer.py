import time
import subprocess
import json
import logging
from datetime import datetime
import os

# 切换到脚本所在目录，确保能够正确调用 fetchMentions.sh
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("comments.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def fetch_and_log_comments():
    try:
        # 执行 fetchMentions.sh
        result = subprocess.run(["sh", "fetchMentions.sh"], capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        
        if not output:
            logging.warning("fetchMentions.sh 没有返回任何内容。")
            return

        # 解析 JSON
        try:
            data = json.loads(output)
        except json.JSONDecodeError:
            # shell 脚本中可能包含一些其他的输出，尝试只取大括号包裹的部分
            output = output[output.find('{'):output.rfind('}')+1]
            data = json.loads(output)
        
        if data.get("success"):
            message_list = data.get("data", {}).get("message_list", [])
            logging.info(f"====== 获取到 {len(message_list)} 条评论通知 ======")
            
            for msg in message_list:
                user_name = msg.get("user_info", {}).get("nickname", "未知用户")
                title = msg.get("title", "通知")
                comment_content = msg.get("comment_info", {}).get("content", "")
                note_content = msg.get("item_info", {}).get("content", "未知笔记内容")
                note_content = note_content.replace('\n', ' ')[:20] + '...' if len(note_content) > 20 else note_content
                
                log_message = f"[{title}] {user_name} 评论: \"{comment_content}\" 👉 笔记: \"{note_content}\""
                
                # 如果有目标评论（针对某条特定评论的回复）
                target_comment = msg.get("comment_info", {}).get("target_comment", {}).get("content")
                if target_comment:
                    log_message += f" | 引用你的评论: \"{target_comment}\""
                    
                logging.info(log_message)
        else:
            logging.error(f"接口返回失败: {data.get('msg', '未知错误')}")
            
    except subprocess.CalledProcessError as e:
        logging.error(f"执行 fetchMentions.sh 失败: {e.stderr}")
    except json.JSONDecodeError as e:
        logging.error(f"JSON 解析失败: {e} - 返回内容: {output}")
    except Exception as e:
        logging.error(f"发生未知错误: {e}")

if __name__ == "__main__":
    logging.info("启动评论获取定时器，轮询频率：1分钟/次...")
    # 立即执行一次
    fetch_and_log_comments()
    # 每隔一分钟执行一次
    while True:
        time.sleep(60)
        fetch_and_log_comments()
