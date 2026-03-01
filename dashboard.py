"""
dashboard.py - 简单的 HTTP 服务，用于查看 SQLite 数据库中消息的状态
无外部依赖，仅使用 Python 标准库。
"""
import json
import sqlite3
import re
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from message_store import get_connection, get_stats

DB_PATH = Path(__file__).parent / "messages.db"
AUTH_FILE = Path(__file__).parent / "doc" / "auth.json"


def parse_curl_to_auth(curl_text: str) -> dict:
    auth = {}
    cookie_match = re.search(r"-b\s+'([^']+)'", curl_text) or re.search(r'-b\s+"([^"]+)"', curl_text)
    if cookie_match:
        auth["cookie"] = cookie_match.group(1)
        
    headers_to_extract = ["x-s", "x-s-common", "x-t", "x-b3-traceid", "x-xray-traceid"]
    for header in headers_to_extract:
        pattern = rf"-H\s+'{header}:\s*([^']+)'"
        match = re.search(pattern, curl_text, re.IGNORECASE)
        if not match:
             pattern = rf'-H\s+"{header}:\s*([^"]+)"'
             match = re.search(pattern, curl_text, re.IGNORECASE)
        if match:
             auth[header.replace("-", "_")] = match.group(1)
    return auth


def update_auth(fetch_curl: str, reply_curl: str):
    if not AUTH_FILE.exists():
        current_data = {"fetch": {}, "reply": {}}
    else:
        try:
            with open(AUTH_FILE, "r", encoding="utf-8") as f:
                current_data = json.load(f)
        except Exception:
            current_data = {"fetch": {}, "reply": {}}
            
    if fetch_curl.strip():
        fetch_auth = parse_curl_to_auth(fetch_curl)
        if fetch_auth:
             current_data["fetch"].update(fetch_auth)
             
    if reply_curl.strip():
        reply_auth = parse_curl_to_auth(reply_curl)
        if reply_auth:
             current_data["reply"].update(reply_auth)
             
    current_data["updated_at"] = datetime.now().isoformat()
    
    with open(AUTH_FILE, "w", encoding="utf-8") as f:
        json.dump(current_data, f, indent=4)
        
    return current_data


def get_recent_messages(limit=50):
    conn = get_connection()
    rows = conn.execute("""
        SELECT id, type, user_nickname, comment_content, note_content, target_comment_content, status, created_at, processed_at
        FROM messages
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            stats = get_stats()
            messages = get_recent_messages(50)
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>小红书评论获取 - 监控面板</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; margin: 20px; background-color: #f5f5f5; color: #333; }}
                    h1, h2 {{ color: #ff2442; }}
                    .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; }}
                    .stats {{ display: flex; gap: 20px; flex-wrap: wrap; }}
                    .stat-box {{ background: #f0f8ff; padding: 15px; border-radius: 8px; border-left: 4px solid #0066cc; min-width: 150px; flex: 1; }}
                    .stat-box.pending {{ border-color: #ff9800; background: #fff8f0; }}
                    .stat-box.done {{ border-color: #4caf50; background: #f0fdf4; }}
                    .stat-box.failed {{ border-color: #f44336; background: #fff0f0; }}
                    .stat-number {{ font-size: 24px; font-weight: bold; margin-top: 5px; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); background: white; }}
                    th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; word-break: break-all; }}
                    th {{ background-color: #fafafa; font-weight: bold; color: #555; }}
                    tr:hover {{ background-color: #f9f9f9; }}
                    .status-badge {{ padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; display: inline-block; text-align: center; min-width: 60px; }}
                    .status-pending {{ background-color: #ffcc80; color: #e65100; }}
                    .status-processing {{ background-color: #81d4fa; color: #01579b; }}
                    .status-done {{ background-color: #a5d6a7; color: #1b5e20; }}
                    .status-failed {{ background-color: #ef9a9a; color: #b71c1c; }}
                    .type-badge {{ font-size: 12px; padding: 2px 6px; border-radius: 4px; background: #eee; color: #666; margin-bottom: 4px; display: inline-block; }}
                    .timestamp {{ font-family: monospace; color: #666; font-size: 12px; }}
                    .truncate-2 {{ display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
                </style>
                <script>
                    // 自动刷新页面内容
                    function fetchData() {{
                        fetch('/api/data')
                            .then(response => response.json())
                            .then(data => {{
                                // 更新统计
                                document.getElementById('stat-total').innerText = Object.values(data.stats).reduce((a, b) => a + b, 0);
                                document.getElementById('stat-pending').innerText = data.stats['pending'] || 0;
                                document.getElementById('stat-processing').innerText = data.stats['processing'] || 0;
                                document.getElementById('stat-done').innerText = data.stats['done'] || 0;
                                document.getElementById('stat-failed').innerText = data.stats['failed'] || 0;
                                
                                // 更新表格
                                const tbody = document.getElementById('messages-body');
                                tbody.innerHTML = '';
                                data.messages.forEach(msg => {{
                                    const tr = document.createElement('tr');
                                    
                                    const statusClass = 'status-' + msg.status;
                                    let contentHtml = '';
                                    if(msg.type === 'comment/comment') {{
                                        contentHtml = `<div class="type-badge">回复评论</div><br>
                                                       <div class="truncate-2" title="${{msg.target_comment_content || ''}}"><small>原评：${{msg.target_comment_content || ''}}</small></div>
                                                       <div style="margin-top:4px;"><b>${{msg.comment_content || ''}}</b></div>`;
                                    }} else {{
                                        contentHtml = `<div class="type-badge">评论笔记</div><br>
                                                       <div style="margin-top:4px;"><b>${{msg.comment_content || ''}}</b></div>`;
                                    }}
                                    
                                    const noteTitleHtml = `<div class="truncate-2" title="${{msg.note_content}}">${{msg.note_content || ''}}</div>`;
                                    
                                    tr.innerHTML = `
                                        <td><span class="status-badge ${{statusClass}}">${{msg.status}}</span></td>
                                        <td>${{msg.user_nickname || ''}}</td>
                                        <td>${{contentHtml}}</td>
                                        <td>${{noteTitleHtml}}</td>
                                        <td><div class="timestamp">${{msg.created_at || ''}}</div><div class="timestamp" style="color:#aaa;">${{msg.processed_at || ''}}</div></td>
                                    `;
                                    tbody.appendChild(tr);
                                }});
                            }})
                            .catch(error => console.error('Error fetching data:', error));
                    }}
                    
                    // 每 5 秒刷新一次
                    setInterval(fetchData, 5000);
                </script>
            </head>
            <body>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h1>🍌 消息监控面板</h1>
                    <a href="/auth" style="padding: 8px 16px; background: #ff2442; color: white; text-decoration: none; border-radius: 4px; font-weight: bold;">🔑 认证管理</a>
                </div>
                
                <div class="card">
                    <h2>整体统计</h2>
                    <div class="stats">
                        <div class="stat-box">
                            <div>总消息数</div>
                            <div class="stat-number" id="stat-total">{sum(stats.values())}</div>
                        </div>
                        <div class="stat-box pending">
                            <div>待处理 (Pending)</div>
                            <div class="stat-number" id="stat-pending">{stats.get('pending', 0)}</div>
                        </div>
                        <div class="stat-box">
                            <div>处理中 (Processing)</div>
                            <div class="stat-number" id="stat-processing">{stats.get('processing', 0)}</div>
                        </div>
                        <div class="stat-box done">
                            <div>已完成 (Done)</div>
                            <div class="stat-number" id="stat-done">{stats.get('done', 0)}</div>
                        </div>
                        <div class="stat-box failed">
                            <div>失败 (Failed)</div>
                            <div class="stat-number" id="stat-failed">{stats.get('failed', 0)}</div>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <h2>最近消息 (Top 50)</h2>
                    <table>
                        <thead>
                            <tr>
                                <th style="width: 100px;">状态</th>
                                <th style="width: 120px;">用户</th>
                                <th style="width: 35%;">评论内容</th>
                                <th style="width: 25%;">对应笔记</th>
                                <th style="width: 160px;">时间(创建/处理)</th>
                            </tr>
                        </thead>
                        <tbody id="messages-body">
            """
            for msg in messages:
                status_class = f"status-{msg['status']}"
                
                if msg['type'] == 'comment/comment':
                    content_html = f"""<div class="type-badge">回复评论</div><br>
                                       <div class="truncate-2" title="{msg.get('target_comment_content', '')}"><small>原评：{msg.get('target_comment_content', '')}</small></div>
                                       <div style="margin-top:4px;"><b>{msg.get('comment_content', '')}</b></div>"""
                else:
                    content_html = f"""<div class="type-badge">评论笔记</div><br>
                                       <div style="margin-top:4px;"><b>{msg.get('comment_content', '')}</b></div>"""
                                       
                note_html = f"""<div class="truncate-2" title="{msg.get('note_content', '')}">{msg.get('note_content', '')}</div>"""
                
                html += f"""
                            <tr>
                                <td><span class="status-badge {status_class}">{msg['status']}</span></td>
                                <td>{msg.get('user_nickname', '')}</td>
                                <td>{content_html}</td>
                                <td>{note_html}</td>
                                <td><div class="timestamp">{msg.get('created_at', '')}</div><div class="timestamp" style="color:#aaa;">{msg.get('processed_at', '') or ''}</div></td>
                            </tr>
                """
            html += """
                        </tbody>
                    </table>
                </div>
            </body>
            </html>
            """
            
            self.wfile.write(html.encode('utf-8'))
            
        elif self.path == '/api/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.end_headers()
            
            stats = get_stats()
            messages = get_recent_messages(50)
            data = {"stats": stats, "messages": messages}
            
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/auth':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            try:
                with open(AUTH_FILE, "r", encoding="utf-8") as f:
                    auth_data = json.load(f)
                updated_at = auth_data.get("updated_at", "未知")
            except:
                updated_at = "暂无"

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>认证管理 - 小红书评论系统</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: 'PingFang SC', sans-serif; margin: 20px; background-color: #f5f5f5; color: #333; }}
                    h1, h2 {{ color: #ff2442; }}
                    .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; max-width: 800px; margin: 0 auto; }}
                    textarea {{ width: 100%; height: 150px; padding: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; font-family: monospace; font-size: 13px; resize: vertical; margin-bottom: 10px; }}
                    button {{ background-color: #ff2442; color: white; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 4px; cursor: pointer; }}
                    button:hover {{ background-color: #e61b36; }}
                    .success-msg {{ color: #4caf50; font-weight: bold; display: none; margin-top: 10px; }}
                    .nav-link {{ color: #666; text-decoration: none; margin-bottom: 20px; display: inline-block; }}
                    .nav-link:hover {{ text-decoration: underline; }}
                </style>
                <script>
                    function submitAuth() {{
                        const fetchCurl = document.getElementById('fetch-curl').value;
                        const replyCurl = document.getElementById('reply-curl').value;
                        
                        document.getElementById('submit-btn').disabled = true;
                        document.getElementById('submit-btn').innerText = '保存中...';
                        
                        fetch('/api/auth', {{
                            method: 'POST',
                            headers: {{
                                'Content-Type': 'application/json',
                            }},
                            body: JSON.stringify({{ fetch_curl: fetchCurl, reply_curl: replyCurl }}),
                        }})
                        .then(response => response.json())
                        .then(data => {{
                            document.getElementById('submit-btn').disabled = false;
                            document.getElementById('submit-btn').innerText = '保存并更新';
                            
                            const msg = document.getElementById('success-msg');
                            msg.style.display = 'block';
                            if (data.updated_at) {{
                                document.getElementById('updated-time').innerText = data.updated_at;
                            }}
                            
                            // 清空输入框
                            document.getElementById('fetch-curl').value = '';
                            document.getElementById('reply-curl').value = '';
                            
                            setTimeout(() => {{ msg.style.display = 'none'; }}, 3000);
                        }})
                        .catch(error => {{
                            console.error('Error:', error);
                            alert('保存失败，请查看控制台');
                            document.getElementById('submit-btn').disabled = false;
                            document.getElementById('submit-btn').innerText = '保存并更新';
                        }});
                    }}
                </script>
            </head>
            <body>
                <div class="card">
                    <a href="/" class="nav-link">← 返回监控面板</a>
                    <h2>🔑 认证信息管理</h2>
                    <p style="color: #666;">上次更新时间：<span id="updated-time" style="font-weight: bold;">{updated_at}</span></p>
                    <p style="font-size: 14px; background: #fff8f0; padding: 10px; border-left: 4px solid #ff9800;">
                        使用说明：请在浏览器开发者工具 (Network) 中，找到请求，右键 -> <b>Copy as cURL</b>，然后将整个 cURL 命令粘贴到下方对应的文本框中。系统会自动解析 Cookie 和 Header 签名参数。
                    </p>
                    
                    <div style="margin-top: 20px;">
                        <h3>1. 拉取评论消息 (Fetch Mentions)</h3>
                        <p style="font-size: 12px; color: #888; margin-top:-10px;">对应请求: <code>/api/sns/web/v1/you/mentions</code></p>
                        <textarea id="fetch-curl" placeholder="粘贴完整的 cURL 命令 (curl 'https://edith.xiaohongshu.com/api/sns/web/v1/you/mentions...')..."></textarea>
                    </div>
                    
                    <div style="margin-top: 15px;">
                        <h3>2. 回复评论 (Reply Comment)</h3>
                        <p style="font-size: 12px; color: #888; margin-top:-10px;">对应请求: <code>/api/sns/web/v1/comment/post</code></p>
                        <textarea id="reply-curl" placeholder="粘贴完整的 cURL 命令 (curl 'https://edith.xiaohongshu.com/api/sns/web/v1/comment/post...')..."></textarea>
                    </div>
                    
                    <div style="margin-top: 20px;">
                        <button id="submit-btn" onclick="submitAuth()">保存并更新</button>
                        <div id="success-msg" class="success-msg">✅ 认证信息已成功解析并保存生效！</div>
                    </div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/auth':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            try:
                data = json.loads(post_data)
                fetch_curl = data.get("fetch_curl", "")
                reply_curl = data.get("reply_curl", "")
                
                updated_data = update_auth(fetch_curl, reply_curl)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "updated_at": updated_data.get("updated_at")}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run_dashboard(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DashboardHandler)
    print(f"📊 Web UI 已启动! 请在浏览器访问 http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_dashboard()
# Patch for level 46
