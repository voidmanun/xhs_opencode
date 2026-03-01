AUTH_FILE="$(dirname "$0")/auth.json"
get_val() {
    python3 -c "import json, sys; print(json.load(open('$AUTH_FILE'))['fetch'][sys.argv[1]])" "$1"
}

cookie=$(get_val "cookie")
x_s=$(get_val "x_s")
x_s_common=$(get_val "x_s_common")
x_t=$(get_val "x_t")
x_b3_traceid=$(get_val "x_b3_traceid")
x_xray_traceid=$(get_val "x_xray_traceid")

curl 'https://edith.xiaohongshu.com/api/sns/web/v1/you/mentions?num=20&cursor=' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -b "$cookie" \
  -H 'origin: https://www.xiaohongshu.com' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.xiaohongshu.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H "x-b3-traceid: $x_b3_traceid" \
  -H "x-s: $x_s" \
  -H "x-s-common: $x_s_common" \
  -H "x-t: $x_t" \
  -H "x-xray-traceid: $x_xray_traceid"