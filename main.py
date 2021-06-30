from flask import Flask, render_template, url_for, request, redirect, session
from news import news         #导入news蓝图
from user import  user        #导入user蓝图
from product import product   #导入product蓝图
app=Flask(__name__)
app.secret_key='any random string'
urls=[news,user,product]      #将三个路由构建数组
for url in urls:
    app.register_blueprint(url)   #将三个路由均实现蓝图注册到主app应用上

@app.route('/')
def index():
    userinfo=''
    return render_template("index.html",data=userinfo)

if __name__=="__main__":
    print(app.url_map)                 #打印url结构图
    app.run(port=2020,host="127.0.0.1",debug=True)