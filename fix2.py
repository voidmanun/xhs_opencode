with open('dashboard.py', 'r') as f:
    content = f.read()

content = content.replace('''        elif self.path == "/api/skip":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(post_data)
                msg_id = data.get("id")
                if not msg_id:
                    raise ValueError("消息 ID 不能为空")
                from message_store import update_status
                update_status(msg_id, "ignored")
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))

            self.send_response(404)
            self.end_headers()''', '''        elif self.path == "/api/skip":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(post_data)
                msg_id = data.get("id")
                if not msg_id:
                    raise ValueError("消息 ID 不能为空")
                from message_store import update_status
                update_status(msg_id, "ignored")
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()''')

with open('dashboard.py', 'w') as f:
    f.write(content)
