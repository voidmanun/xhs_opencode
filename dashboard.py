"""
dashboard.py - 简单的 HTTP 服务，用于查看 SQLite 数据库中消息的状态
无外部依赖，仅使用 Python 标准库。
"""
import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from message_store import get_connection, get_stats

DB_PATH = Path(__file__).parent / "messages.db"

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
                <h1>🍌 消息监控面板</h1>
                
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
