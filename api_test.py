import requests
from flask import Flask, render_template, request, redirect, url_for, session
from flask import g  #方式全局g对象和context处理。
from sqlite_test import dbUtils #导入dbutil模块

from flask_cors import cross_origin
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@cross_origin()
def get_tasks():
    r = requests.get("http://m.xcx.hntsjkj.cn/v1/api/shop/list", params=request.values.to_dict())
    print(request.form)
    print(request.data)
    print(request.method)
    # print("cadasd====",request.values.to_dict()['a'])  #存储有query值
    print(request.headers)
    print(request.args)
    print(request.json)
    print(r.json()['data']['list'])

    return jsonify({'data': r.json()['data']['list']})

if __name__ == '__main__':
    app.run(debug=True)

# if __name__=="__main__":
#     param = {
#         'app_id': 'th23o66be7697cf38',
#         'sign': '2a0025d4d408fcaac6b2bd8e4e489256'
#     }
#
#     r = requests.get("http://m.xcx.hntsjkj.cn/v1/api/shop/list", params=param)
#
#     print(r.json()['data']['list'][1])