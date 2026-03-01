import sys
import json
import time
import logging
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [PlaywrightReply] %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

AUTH_FILE = Path(__file__).parent / "auth.json"

def get_cookies_from_auth():
    """解析 auth.json 里的 cookie 字符串，转换为 playwright 可用的 cookie 列表"""
    try:
        with open(AUTH_FILE, "r", encoding="utf-8") as f:
            auth_data = json.load(f).get("reply", {})
        
        cookie_str = auth_data.get("cookie", "")
        if not cookie_str:
            logger.error("在 auth.json 中找不到 'reply' 的 cookie！")
            return []       
            
        cookies = []
        for item in cookie_str.split(";"):
            item = item.strip()
            if "=" in item:
                k, v = item.split("=", 1)
                cookies.append({
                    "name": k,
                    "value": v,
                    "domain": ".xiaohongshu.com",
                    "path": "/",
                })
        return cookies
    except Exception as e:
        logger.error(f"读取 auth.json 失败: {e}")
        return []

def run_reply(note_id: str, target_comment_id: str, content: str, xsec_token: str = "", xsec_source: str = "pc_feed"):
    cookies = get_cookies_from_auth()
    if not cookies:
        logger.error("无可用 Cookie，放弃回复。")
        return
        
    logger.info(f"启动浏览器... 目标评论ID: {target_comment_id}")
    logger.info(f"回复内容: {content}")
    logger.info(f"xsec_token: {xsec_token if xsec_token else '未提供'}, xsec_source: {xsec_source}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1440, "height": 900}
        )
        
        context.add_cookies(cookies)
        page = context.new_page()
        try:
            # 1. 访问笔记详情页
            url = f"https://www.xiaohongshu.com/explore/{note_id}"
            if xsec_token:
                url += f"?xsec_token={xsec_token}&xsec_source={xsec_source}"
            logger.info(f"访问笔记详情页: {url}")
            page.goto(url, wait_until="networkidle")
            
            # 等待内容加载
            logger.info("等待页面加载...")
            page.wait_for_timeout(3000)
            
            # 2. 模拟真实滚动，触发评论数据懒加载
            logger.info("向下滚动寻找评论...")
            
            # 智能滚动脚本（派发 WheelEvent），因为普通 Window.scrollBy() 有时不会触发 XHS 的懒加载
            smart_scroll_js = """
            (delta) => {
                let targetElement = document.querySelector('.note-scroller') 
                    || document.querySelector('.interaction-container') 
                    || document.documentElement;
                
                const wheelEvent = new WheelEvent('wheel', {
                    deltaY: delta,
                    deltaMode: 0,
                    bubbles: true,
                    cancelable: true,
                    view: window
                });
                targetElement.dispatchEvent(wheelEvent);
            }
            """
            
            comment_selector = f"#comment-{target_comment_id}"
            comment_element = page.locator(comment_selector).first
            
            # 循环滚动直到找到对应评论
            max_scroll_attempts = 40
            found = False
            for attempt in range(max_scroll_attempts):
                if comment_element.is_visible():
                    found = True
                    logger.info(f"✅ 成功找到评论块: {target_comment_id}")
                    break
                
                # 尝试展开所有被折叠的子评论，防止目标评论被隐藏
                try:
                    for btn in page.locator(".show-more").all():
                        if btn.is_visible():
                            try:
                                btn.click(timeout=1000)
                                page.wait_for_timeout(300)
                            except Exception:
                                pass
                except Exception:
                    pass
                
                # 执行智能滚动
                page.evaluate(smart_scroll_js, 500)
                # 同时也试一下原生 scroll 兜底
                page.mouse.wheel(0, 500)
                page.wait_for_timeout(1000)
                
            if not found:
                logger.error(f"在页面上滑动了 {max_scroll_attempts} 次仍未能找到对应的目标评论: {target_comment_id}")
                page.screenshot(path="playwright_error_comment_not_found.png")
                sys.exit(1)
                
            # 3. 找到评论后，让其完整显示
            comment_element.scroll_into_view_if_needed()
            page.wait_for_timeout(1000)
            
            # 在对应的评论区域内找到并点击回复按钮
            reply_btn = comment_element.locator(".right .interactions .reply").first
            if reply_btn.is_visible():
                logger.info("点击目标评论的回复按钮")
                reply_btn.click()
                page.wait_for_timeout(1000)
            else:
                logger.error("未找到回复按钮元素，可能没有权限或者DOM结构已变更")
                page.screenshot(path="playwright_error_no_reply_btn.png")
                sys.exit(1)
                
            # 4. 在底部的回复文本框中输入内容
            logger.info("寻找输入框并填写回复...")
            input_box = page.locator("div.input-box div.content-edit p.content-input").first
            
            if not input_box.is_visible():
                input_box = page.locator("#content-textarea").first
                
            if input_box.is_visible():
                input_box.click()
                page.wait_for_timeout(500)
                page.keyboard.type(content, delay=50)
                logger.info("已填写评论内容")
            else:
                logger.error("未找到输入框")
                page.screenshot(path="playwright_error_no_input.png")
                sys.exit(1)
                
            page.wait_for_timeout(1000)
            
            # 5. 点击发送
            submit_btn = page.locator("div.bottom button.submit").first
            if submit_btn.is_visible():
                submit_btn.click()
                logger.info("✅ 已点击发送/提交按钮，完成自动回复。")
                page.wait_for_timeout(3000)  # 等待请求发出
            else:
                logger.error("找不到提交/发送按钮")
                page.screenshot(path="playwright_error_no_submit_btn.png")
                sys.exit(1)
                
            # 成功记录
            page.screenshot(path="playwright_success.png")

        except Exception as e:
            logger.error(f"自动化执行异常: {e}")
            page.screenshot(path="playwright_error_screenshot.png")
            sys.exit(1)
        finally:
            browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: python3 {sys.argv[0]} <note_id> <target_comment_id> <content> [xsec_token]")
        sys.exit(1)
        
    note_id = sys.argv[1]
    target_comment_id = sys.argv[2]
    content = sys.argv[3]
    xsec_token = sys.argv[4] if len(sys.argv) > 4 else ""
    xsec_source = sys.argv[5] if len(sys.argv) > 5 else "pc_feed"
    
    run_reply(note_id, target_comment_id, content, xsec_token, xsec_source)
