with open('dashboard.py', 'r') as f:
    content = f.read()

content = content.replace('''                    function skipMessage(id) {
                        if (confirm("确定要跳过这条消息吗？")) {
                            fetch("/api/skip", {
                                method: "POST",
                                headers: { "Content-Type": "application/json" },
                                body: JSON.stringify({ id: id })
                            })
                            .then(response => response.json())
                            .then(data => {
                                if (data.success) {
                                    fetchData();
                                } else {
                                    alert("跳过失败: " + data.error);
                                }
                            })
                            .catch(error => console.error("Error:", error));
                        }
                    }''', '''                    function skipMessage(id) {{
                        if (confirm("确定要跳过这条消息吗？")) {{
                            fetch("/api/skip", {{
                                method: "POST",
                                headers: {{ "Content-Type": "application/json" }},
                                body: JSON.stringify({{ id: id }})
                            }})
                            .then(response => response.json())
                            .then(data => {{
                                if (data.success) {{
                                    fetchData();
                                }} else {{
                                    alert("跳过失败: " + data.error);
                                }}
                            }})
                            .catch(error => console.error("Error:", error));
                        }}
                    }}''')

with open('dashboard.py', 'w') as f:
    f.write(content)
