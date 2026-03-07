import subprocess
import os
import sys

def main():
    print("=========================================")
    print("手动测试 Opencode Agent")
    print("输入你的 message（输入 'exit' 或 'quit' 退出）")
    print("=========================================")
    
    while True:
        try:
            comment = input("\n[输入]: ")
            if not comment.strip():
                continue
                
            if comment.lower() in ('exit', 'quit'):
                print("退出程序。")
                break
                
            print(f"🚀 正在发送消息给 gamemaker agent: '{comment}'")
            
            opencode_path = "/root/.opencode/bin/opencode"
            if not os.path.exists(opencode_path):
                opencode_path = "opencode"  # fallback
                
            cmd_str = f"{opencode_path} run --agent gamemaker '{comment}'"
            
            # 这里调用逻辑同 consumer.py 中的调用
            result = subprocess.run(
                cmd_str,
                shell=True,
                capture_output=True,
                text=True,
                check=False,
                cwd="/root/workspace/share_game"
            )

            if result.returncode != 0:
                print(f"❌ gamemaker 处理失败 (code {result.returncode})。\n错误信息:\n{result.stderr.strip()}")
            else:
                reply_content = result.stdout.strip()
                print(f"✅ gamemaker 处理成功。返回结果:\n{reply_content}")
                
        except KeyboardInterrupt:
            print("\n退出程序。")
            break
        except EOFError:
            print("\n退出程序。")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    main()
