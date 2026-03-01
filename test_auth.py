import dashboard
curl_text = """curl 'https://edith.xiaohongshu.com/api/sns/web/v1/comment/post' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'content-type: application/json;charset=UTF-8' \
  -b 'abRequestId=c82008a1-1d6b-5d53-8133-b054ce35e50a; a1=19c9ed88a52aw639z86vixcm16cqo9uo2xtk7twsg30000172510; webId=99fc22e462615269bacd9b479b4ed072; gid=yjSjdfYjSSJyyjSjdfYY0C9E2J0EKqjuYKh39MkCS6yKSTq8Alj7lW888yWJ2y88WdYSfS2S; web_session=04006979cf9feb154835c3ed943b4bafdeac88; id_token=VjEAADXMBHjchkQx05IR7LUsnTYjJS0Z54/2l8JboLoPvwzNKao3QqoB9DavUHcuVB01u/XVgNSXAxT4uwka3GSKmpoHJze0Nio97nPeMD+yUwZqT+edYZb9Q4OA0rb/0BjfYOyV; webBuild=5.13.0; customer-sso-sid=68c5176121620342776135680y9alexu8mnzd5ur; x-user-id-creator.xiaohongshu.com=5b11e34711be10479b461863; customerClientId=428843771153632; access-token-creator.xiaohongshu.com=customer.creator.AT-68c517612162034277580801oopsdzs1cmdkmvkf; galaxy_creator_session_id=ywiujqnxPkJqEoGdfncLIVEPckQLsJP2S174; galaxy.creator.beaker.session.id=1772344586103075249053; xsecappid=xhs-pc-web; acw_tc=0ad6fb2117723509282465759e95e8dbed4dcb84e0f945d303017404589a4f; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=0805bc4d-820d-4aaa-98de-a3a701850baa; loadts=1772351585816' \
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
  -H 'x-b3-traceid: 68142391a3e8a165' \
  -H 'x-s: XYS_2UQhPsHCH0c1PUhlHjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHfM1qAZAPebK8MQYa7bz8FbMJDSkabpL/FLAPBSDaem0+/zwGSHh+p8Ta9khnnDha/QxPoL7a/zDpL4UpFkO+B4C8pmz2gZF/b+MJ9bepDMCPem1wok3/Spn4e8sJ7WlyoGUwLT7pBM+49Sia/DhppYs8A8U/Bql8aV78MLIaDYNnb+tnDlo+0LlprMeJdmALdkaaSmpGpcAJemhaM+18b8yJB+kz/mtLDS3PrRH/SQaprM0yrGFcfElnfRntMpn8oQEpDYdpn4fHjIj2ecjwjQ6GfkSG7cjKc==' \
  -H 'x-s-common: 2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0c1PUhlHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0L1P/P1PsHVHdWMH0ijP/S0wnpDweYY+/QY4AGAwgih+d8k2B+TP/80qnuE4nuU2oz3+7z7q9qAPeZIPer7P0LlPsHVHdW9H0ijHjIj2eqjwjHjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL08z/sVManD9q9z18np/8db8aob7JeQl4epsPrzsagW3tF4ryaRApdz3agYDq7YM47HFqgzkanYMGLSbP9LA/bGIa/+nprSe+9LI4gzVPDbrJg+P4fprLFTALMm7+LSb4d+kpdzt/7b7wrQM498cqBzSpr8g/FSh+bzQygL9nSm7qSmM4epQ4flY/BQdqA+l4oYQ2BpAPp87arS34nMQyFSE8nkdqMD6pMzd8/4SL7bF8aRr+7+rG7mkqBpD8pSUzozQcA8Szb87PDSb/d+/qgzVJfl/4LExpdzQ4fRSy7bFP9+y+7+nJAzdaLp/2LSiz/YHwgbMagYiJdbCwB4QyFSfJ7b7yFSenS4o+A+A8BlO8p8c4A+Q4DbSPB8d8nzfJrkQy/pAPFMUJeQM4rbQyLTAynz98nTy/fpLLocFJDbO8p4c4FpQ4SSYG9pm8nzn4MYd8DEAL7p7LrDALdQQ2rLM/op749bl4UTU8nTinDbw8/b+/fLILoqEaL+wqM8PJ9p/GDSBanT6qM+U+7+nJD8kanTdqM8n4rMQygpDqgb7t7zl4b4QPAmSPMm7aLSiJ9LA4gclanSOq9kM4e+74gz1qMm7nrSeG9lQPFSUP04VyAQQ+nLl4gzeaLp/NFSbadPILoz1qbSQcLuIafp88DclaLpULrRc4rT6qgqAa/+O8gYl4b4z/epSygk9qA+P/npQzLkApf8O8/+l4omP4g4lag898n8n4FpQynpS2emn4FSe8Bp/cfpSPbmFnrSh4d+3qgq9wBz+qLSiaaTQPApA+dH98nT1afpDG08AyS8F2DSbqL8QP9V9qM8FJFSk/BSQyLkSPFSTpBEfN9pxqg4CanTinB+c47YOqB4SL7k6q7Yn4BStqgzVanSywrSeL7QTqgc3Lp878LSh4d+DJLkSPobFa9bc494QygH3qSmF+DSkpom68DpAaLLA8p+f/7+kpnRSPp8F2/zc4FEQznT6agYmq9Tn4okQ4fpSpSP3GDS9JgkFy0zGaL+bNFS9J9pDpdq7qgpFaSmn4b4Q2rSyanWAq7YS/9phqg4yqrlQLFSez9zYpdzrGS8FpLShGFYQyFz6aLp3qrSiad+nG08A2BQ//gzl4URQyB+mGMm72nQn4FbQyrTS+DQgyrShp04P8epS8dpFwgQn4BRjpF8UnfRyzrSkJrI6pd4SanTDq7Y0zLlQyMPUq7b74rShqo8jpdzlLbmFwLSeLBRQzLM1aLpzzrYM4MmQyrYyHjIj2eDjw0HMPeqhweqhPaIj2erIH0iINsQhP/rjwjQ1J7QTGnIjNsQhP/HjwjHl+AqUPALl+/W9P0rIwAr7+AHlweHIweDMw/PjKc==' \
  -H 'x-t: 1772351603887' \
  -H 'x-xray-traceid: ce5431a25027e12ab06d4d4408ec713b' \
  --data-raw '{"note_id":"69a3e092000000001a027ba6","target_comment_id":"69a3f00c000000000f029078","content":"满意不","at_users":[]}'"""

print("Updating auth.json...")
dashboard.update_auth(curl_text)
print("Done!")
