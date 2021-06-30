import requests
import json
import  sqlite_test

data = {
    'sAccount': 'visitor1',
    'sPasswd': 'Mk6Hfqrmli'
}

body = {
    "statisticType": "hour",
    "items": [
        "PH",
        "WT",
        "DOX",
        "CODMN",
        "CHLA",
        "NH3N",
        "TN",
        "TP",
        "VLPH",
        "TAS",
        "COD",
        "TK",
        "FTU"
    ],
    "pageNo": 1,
    "pageSize": 10,
    "wetlandId": "",
    "stationId": [
        "1262591067912404993"
    ],
    "startTime": "1617206400",
    "endTime": "1617983999"
}

# http://221.182.193.126:8769/uaa/loginTokenWeb?sAccount=sAccount&sPasswd=Mk6Hfqrmli
r = requests.post("http://221.182.193.126:8769/uaa/loginTokenWeb", params=data)

headers = {'Authorization': r.json()['data']['token_type']+' '+ r.json()['data']['access_token'],
           'Content-Type': 'application/json'
           }
r1 = requests.post("http://221.182.193.126:8769/service-meta-monitor/cttnet/tWaterQualityDataHistoryController/listWaterQualityDataHistory",
                   headers=headers, data = json.dumps(body))
# print(r.content)  # r.content表示二进制流
# print(r.json())    #r.json表示json对象
print(r1.json())    #r1.json表示json对象

for i in r1.json()['data']['records']:
    print('wetlandName:',i['wetlandName'],' stationName:',i['stationName'],
          ' dataType',i['dataType'],' stationId',i['stationId'],' stationType',i['stationType'],
          ' time',i['time'])

#1.创建数据库
db=sqlite_test.dbUtils('web2020.db')
for i in r1.json()['data']['records']:
    sql= "insert into wetland ('wetlandName', 'stationName', 'dataType', 'stationId') values('{0}', '{1}', '{2}', '{3}');". \
        format(i['wetlandName'], i['stationName'], i['dataType'], i['stationId'])
    print(sql)
    if db.db_action(sql,0) == True:
        print("新增新闻表成功！")
    else:
        print("try again1")

db.close()
