#!/bin/bash

echo "🔄 正在准备重启小红书评论系统..."

# 查找所有 run.py 相关的进程，排除 grep 自身，并获取 PID
PIDS=$(ps aux | grep "[p]ython3 run.py" | awk '{print $2}')

if [ -n "$PIDS" ]; then
    echo "🛑 找到正在运行的系统进程，正在关闭..."
    for PID in $PIDS; do
        echo "终止进程 PID: $PID"
        kill -9 $PID 2>/dev/null
    done
    echo "✅ 旧进程已关闭！"
else
    echo "ℹ️ 未发现正在运行的系统进程。"
fi

# 确保端口 8080 被释放 (以防万一是被其他程序占用)
PORT_PID=$(lsof -t -i:8080)
if [ -n "$PORT_PID" ]; then
    echo "⚠️ 发现端口 8080 仍被占用 (PID: $PORT_PID)，强制释放..."
    kill -9 $PORT_PID 2>/dev/null
fi

echo "🚀 重新启动系统 (后台运行)..."
# 使用 nohup 后台运行，日志追加到 run.log
nohup python3 run.py > run.log 2>&1 &

echo ""
echo "🎉 重启成功！"
echo "👉 后台日志可查看: tail -f run.log"
echo "👉 Dashboard 地址: http://localhost:8080"
echo "👉 认证管理地址: http://localhost:8080/auth"
