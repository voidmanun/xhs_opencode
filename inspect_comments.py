from playwright.sync_api import sync_playwright
import json

def get_cookies_from_auth():
    try:
        with open("/root/workspace/xhs_opencode/doc/auth.json", "r", encoding="utf-8") as f:
            cookie_str = json.load(f).get("reply", {}).get("cookie", "")
        cookies = []
        for item in cookie_str.split(";"):
            item = item.strip()
            if "=" in item:
                k, v = item.split("=", 1)
                cookies.append({"name": k, "value": v, "domain": ".xiaohongshu.com", "path": "/"})
        return cookies
    except Exception:
        return []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    context = browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    context.add_cookies(get_cookies_from_auth())
    page = context.new_page()
    page.goto("https://www.xiaohongshu.com/explore/69a3e092000000001a027ba6?xsec_token=LBggYvuEype3pNFpPtGMaslGEv_dIAjptFubYyCUOaJrQ=&xsec_source=pc_feed", wait_until="networkidle")
    page.wait_for_timeout(3000)
    
    for i in range(20):
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
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)
            
    content = page.content()
    if "那就商店里增加宠物购买吧" in content:
        print("Found text in HTML!")
    else:
        print("Text not found in HTML.")
        
    elements = page.locator(".content").all()
    for el in elements:
        print(el.inner_text())
        
    browser.close()
