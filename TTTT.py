import requests

url = "http://d5ab8e5dd2c24332955d6aed682a4546.apigateway.its.haikou.cn/hk/sjzypt/csfz/getSAPIData?service=WMTS&request=GetTile&version=1.0.0&layer=RESPL_2018&style=default&tilematrixSet=guobiao&format=image2Fpng&height=256&width=256&maxZoom=20&tileSize=256&fullExtent=5Bobject20Object5D&noWrap=true&rowSign=tl&tilematrix=17&tilerow=25642&tilecol=105426"

payload={}
headers = {
    'hnjhpt_sid': 's_2746000000000_14479',
    'hnjhpt_rid': '001@836',
    'hnjhpt_sign': '6rOjH9nuq4gSGmWnYE8H1KRLKWQK6mpU5bKeMd9mmnQ=',
    'hnjhpt_rtime': '1624546813582',
    'Accept-Language': '*/*',
    'Accept-Encoding': '*/*',
    'Accept-Charset': '*/*',
    'Content-Type': '*/*',
    'Accept': '*/*'

}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
