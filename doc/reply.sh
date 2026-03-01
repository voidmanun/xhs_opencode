note_id="$1"
target_comment_id="$2"
content="$3"

curl 'https://edith.xiaohongshu.com/api/sns/web/v1/comment/post' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'content-type: application/json;charset=UTF-8' \
  -b 'abRequestId=c82008a1-1d6b-5d53-8133-b054ce35e50a; xsecappid=xhs-pc-web; a1=19c9ed88a52aw639z86vixcm16cqo9uo2xtk7twsg30000172510; webId=99fc22e462615269bacd9b479b4ed072; gid=yjSjdfYjSSJyyjSjdfYY0C9E2J0EKqjuYKh39MkCS6yKSTq8Alj7lW888yWJ2y88WdYSfS2S; web_session=04006979cf9feb154835c3ed943b4bafdeac88; id_token=VjEAADXMBHjchkQx05IR7LUsnTYjJS0Z54/2l8JboLoPvwzNKao3QqoB9DavUHcuVB01u/XVgNSXAxT4uwka3GSKmpoHJze0Nio97nPeMD+yUwZqT+edYZb9Q4OA0rb/0BjfYOyV; webBuild=5.13.0; acw_tc=0a4ab31917723418104265559ee260da212aec7a211b7026fe3713bd7b857d; websectiga=f47eda31ec99545da40c2f731f0630efd2b0959e1dd10d5fedac3dce0bd1e04d; sec_poison_id=520ff50c-f25c-4b76-ad05-9115cace56aa; loadts=1772342023940' \
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
  -H 'x-b3-traceid: e147e8d43b71ae9f' \
  -H 'x-s: XYS_2UQhPsHCH0c1PUhlHjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHfM1qAZAPebK8MQYa7bC/pSsynRGPLzgpFLAPBSDaLEIygQQGSHh+p81+9khnnDha/QxPBG7a/zDaLIA2/m/zLlDqA+z2gZF/b+MJ9bepDMCPem1wok3/Spn4e8sJ7WlyoGUwLT7pBM+49Sia/DhppYs8A8U/Bql8aV78MLIaDYNnb+tnDlo+0LlprMeJdmALdkaaSmpGpcAJBEhaM+18b8yJB+kz/mtLDS3PrRH/SQaprMj+oLAnoQ++pqMyFVMz7GFyA+VPr+iHjIj2ecjwjQ6GfkSG7cjKc==' \
  -H 'x-s-common: 2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0c1PUhlHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0L1P/P1PsHVHdWMH0ijP/S0wnpDweYY+/QY4AGAwgih+d8k2B+TP/80qnuE4nuU2oz3+7z7q9qAPeZIPer7P0LlPsHVHdW9H0ijHjIj2eqjwjHjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL08z/sVManD9q9z18np/8db8aob7JeQl4epsPrzsagW3tF4ryaRApdz3agYDq7YM47HFqgzkanYMGLSbP9LA/bGIa/+nprSe+9LI4gzVPDbrJg+P4fprLFTALMm7+LSb4d+kpdzt/7b7wrQM498cqBzSpr8g/FSh+bzQygL9nSm7qSmM4epQ4flY/BQdqA+l4oYQ2BpAPp87arS34nMQyFSE8nkdqMD6pMzd8/4SL7bF8aRr+7+rG7mkqBpD8pSUzozQcA8Szb87PDSb/d+/qgzVJfl/4LExpdzQ4fRSy7bFP9+y+7+nJAzdaLp/2LSizLkzwgbMagYiJdbCwB4QyFSfJ7b7yFSenS4o+A+A8BlO8p8c4A+Q4DbSPB8d8nzfJrkQy/pAPFMUJeQM4rbQyLTAynz98nTy/fpLLocFJDbO8p4c4FpQ4SSYG9L78nzl478PwnpAzb87nDDAL7QQ2rLM/op749bl4UTU8nTinDbw8/b+/fLILoqEaL+wqM8PJ9p/GDSBanT6qM+U+7+nJD8kanTdqM8n4rMQygpDqgb7t7zl4b4QPAmSPMm7aLSiJ9LA4gclanSOq9kM4e+74gz1qMm7nrSeG9lQPFSUP04VyAQQ+nLl4gzeaLp/NFSbadPILoz1qbSQcLuIafp88DclaLpULrRc4rT6qgqAa/+O8gYl4b4z/epSygiMq9S+JLlQyLbA2e4SqMzM4oS0Lo4wag8S8p+c4MpQyLES2emPnDSe8Bp/wLkSL7pFPFShP7P9pd4MPf8gcDSb/ezQc94ApDF98nTd8npDnfRA8b8FJLSkz0SQ2BDUJSm7qDShGM+QyLRS8BFF40Qf+nLlqg4janSU2Llc4MYzw/pSPnp9q9Tn4b+oqgzaagYinLSbtMmTpdztaob7aDSk/fpDJrEAygbFaSkl4rQQybPIGM8FPFSeqBbPcD4za/+O8ncEa9LIGLRApdbFq/zc4oSQy7QhanSmqFzn4rzQ4jRSLFMaJDSbJppAJbr6aLL38FSiafpn4g4iGp8F8nRn4BkQ2bmVaLpwqMSS8Bp3pd4mN9EyarSi4aTP4gzdLp8FprS9JL+Qy/YPaLpb/LSb+fLAz0+Ayp+TGMmc47kQc7pbqob7Jpkc4FzQyepSnn8ynLSkqpYI8e8SydpFc9pM4B+6JB+sJM+QyLS3t9YC4g46anV7qAb0LpbQPMbrLob7/rDA2Spypdc347bF8DS9yBEQzpQwaLpgJpk0O/FjNsQhwaHCN/DFPALI+ecAwaIj2erIH0iINsQhP/rjwjQ1J7QTGnIjNsQhP/HjwjHl+AqUPAcUPeHFP/L9wAr7+AHlweHUw/rAP/LjKc==' \
  -H 'x-t: 1772342049542' \
  -H 'x-xray-traceid: ce53e8bd7a5f7fd25357b83e8bda7ca9' \
  --data-raw '{"note_id":"${note_id}","target_comment_id":"${target_comment_id}","content":"${content}","at_users":[]}'