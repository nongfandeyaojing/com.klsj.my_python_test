from flask import Flask, render_template, request, redirect, url_for, session
from flask import g  #方式全局g对象和context处理。
from sqlite_test import dbUtils #导入dbutil模块

# https://zhuanlan.zhihu.com/p/104273184
app = Flask(__name__)



@app.route('/')
# render_template路径一定是要在templates下的文件
# 这里msg为参数值，data为参数名。在html文件中就需要使用jinjia2模板里的数据控制语法
def gotoIndex():
    msg="刘宝盛"
    return render_template("index.html",data=msg)


@app.route('/news')   #增加一个news页面
def newspage():
    # newsContent="全国上下一心支持武汉，武汉加油！"
    # return render_template("news.html",data=newsContent)
    db=dbUtils('web2020.db')     #链接web2020数据库
    sql='select content from news'             #组装查询sql语句
    newslist=db.db_action(sql,1)         #查询处理并返回列表
    print(newslist)
    db.close()                           #关闭数据库
    return render_template("news.html",data=newslist)    #将数据传递到news.html页面中

@app.route('/product/<a>',methods=['GET'])  #增加一个product页面
def productpage(a):
    return render_template("product.html",data=a)

@app.route('/login')
def loginpage():
    return render_template("login.html")


app.secret_key='any random string'    #这里我们直接给定一个密钥,这里要设置这个，不然session用不了
@app.route('/loginProcess',methods=['POST','GET'])
def loginProcesspage():
    if request.method=='POST':
        nm=request.form['nm']     #获取姓名文本框的输入值
        pwd=request.form['pwd']   #获取密码框的输入值
        if nm=='刘宝盛' and pwd=='123':
            session['username']=nm
            #面的跳转先前采用的render_template是不合适的，如果输入的正确时运行后，网页上的url仍然是http://127.0.0.1/loginProcess，而不是首页url，说明render_templates来实现url跳转是不合适的。这里调整一下，选用redirect重定向方式
            return redirect(url_for('gotoIndex'))  #函数gotoIndex
        else:
            return 'the username or userpwd does not match!'

# context上下文处理可以在局部也可以在全局。例如想定义一下全局公用变量，可以采用如下方式：
# @app.context_processor
# def common():
#     isLogin=False
#     return isLogin

# if __name__=='__main__':
#     app.run()