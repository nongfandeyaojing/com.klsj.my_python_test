import configparser
import os
import time
import dingtalk
import json
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Pie

from sqlalchemy.types import VARCHAR, Float, Integer, Date, Numeric
from complite.read_ODPS_Data import Read_ODPS_Data
from complite.data_to_mysql import Data_To_Mysql

from docx.shared import Mm
from docxtpl import DocxTemplate,RichText,InlineImage
from complite.data_to_email import Data_To_Email


# 获取配置文件信息
root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
print(root_dir)
configpath = os.path.join(root_dir, "complite/config.ini")
cf = configparser.ConfigParser()
cf.read(configpath,encoding='utf-8')  # 读取配置文件

# 获取odps信息
access_id = cf.get("ODPS", "access_id")  # 获取[ODPS]access_id信息
secret_access_key = cf.get("ODPS", "secret_access_key")
project = cf.get("ODPS", "project")
endpoint = cf.get("ODPS", "endpoint")
sql1 = cf.get("ODPS", "sql1")  # 查询库的连接性
sql2= cf.get("ODPS", "sql2")  # 重点表巡查
sql2= cf.get("ODPS", "sql2")  # 查询库的连接性
sql2= cf.get("ODPS", "sql2")  # 查询库的连接性
sql3= cf.get("ODPS", "sql3")  # 查询库的连接性
sql4= cf.get("ODPS", "sql4")  # 查询库的连接性
sql5= cf.get("ODPS", "sql5")  # api接口巡检

# 获取mysql信息
host = cf.get("mysql", "host")  # 获取[ODPS]access_id信息
port = cf.get("mysql", "port")
user = cf.get("mysql", "user")
password = cf.get("mysql", "password")
db = cf.get("mysql", "db")  # 查询库的连接性

# 获取
smtp_server = cf.get("email", "smtp_server")
email_user = cf.get("email", "email_user")
email_pass = cf.get("email", "email_pass")
email_port = cf.get("email", "email_port")
sender = cf.get("email", "sender")
receiver = ["gm1-swws7xrmm@dingtalk.com"]
# # html_head = cf.get("email", "html_head")
# html_after = cf.get("email", "html_after")

# 时间
today = time.strftime("%Y-%m-%d", time.localtime())
today_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 文件路径
templa_doc_path = 'resourse/'  #模板路径
day_doc_path = 'resourse/日常监测每日文档/'  #每日监测文档存放路径
day_excel_path = 'resourse/日常监测每日excel/'  #每日监测excel存放路径

if __name__=="__main__":

    # 获取odps数据
    read_ODPS_data = Read_ODPS_Data(access_id,secret_access_key,project,endpoint)
    data1 = read_ODPS_data.sql_odps(sql1)
    print(data1)
    data2 = read_ODPS_data.sql_odps(sql2)
    print(data2)
    data3 = read_ODPS_data.sql_odps(sql3)
    print(data3)
    data4 = read_ODPS_data.sql_odps(sql4)
    print(data4)
    data5 = read_ODPS_data.sql_odps(sql5)
    print(data5)

    '''
        写入到rds/sqlite
    '''
    # d_t_m =  Data_To_Mysql(host=host,port=port,user=user,password=password,db=db)
    # d_t_m.dataFrame_to_msql(df=data1,sql_table='check_db_conn',dtype={"db_name": VARCHAR,"find_time": VARCHAR,"orgin_value": VARCHAR,"today_value": VARCHAR,"if_normal": VARCHAR,},
    #                         index_label=[1,2,3,4,5],  # index_label选择要插入的字段
    #                         insert_type='append')
    # 还是告警啊

    '''
        结果写入xlsx,简单
    '''
    writer = pd.ExcelWriter(day_excel_path+"日常监测"+today+".xlsx")
    data1.to_excel(writer, sheet_name='数据库连通性')
    data2.to_excel(writer, sheet_name='重点表')
    data3.to_excel(writer, sheet_name='rds大屏表检测')
    data4.to_excel(writer, sheet_name='datahub数据流')
    data5.to_excel(writer, sheet_name='API正常性检测')
    writer.save()
    '''
        结果写入到word
    '''
    tpl=DocxTemplate(templa_doc_path+'日常监测模板.docx')
    # docx 富文本插入、样式设计
    context = {
        'today_time': today_time,
        'data1': json.loads(data1.to_json(orient="records")),
        'data2': json.loads(data2.to_json(orient="records")),
        'data3': json.loads(data3.to_json(orient="records")),
        'data4': json.loads(data4.to_json(orient="records")),
        'data5': json.loads(data5.to_json(orient="records")),
    }

    tpl.render(context)
    tpl.save(day_doc_path+"日常监测"+today+".docx")
    '''
        结果发邮件
    '''
    d_t_e = Data_To_Email(smtp_server, email_user, email_pass, email_port)

    df_html1 = d_t_e.df_to_html(data1)
    df_html2 = d_t_e.df_to_html(data2)
    df_html3 = d_t_e.df_to_html(data3)
    df_html4 = d_t_e.df_to_html(data4)
    df_html5 = d_t_e.df_to_html(data5[['id', 'api_name', 'code', 'api_detail', 'date', 'dt']])

    attachments = [
        {
            "filepath": day_doc_path+"日常监测"+today+".docx",
            "filename": "日常监测"+today+".docx",
            "email_type": ""
        },
        {
            "filepath": day_excel_path+"日常监测"+today+".xlsx",
            "filename": "日常监测"+today+".xlsx",
            "email_type": ""
        },
        {
            "filepath": templa_doc_path+"邮件数据图片.jpg",
            "filename": "邮件数据图片.jpg",
            "email_type": "image",
            "id": "0"
        },
    ]
    d_t_e.send_Email(sender=sender, subject="数据资源平台巡检日报", context_html=d_t_e.html_head+'<h2><img src="cid:0"></h2>'
                                                                + '<h2>1.数据库连通性</h2>'+df_html1
                                                                + '<h2>2.重点表</h2>'+df_html2
                                                                + '<h2>3.rds大屏表检测</h2>'+df_html3
                                                                + '<h2>4.datahub数据流</h2>'+df_html4
                                                                + '<h2>5.API正常性检测</h2>'+df_html5
                                                                + d_t_e.html_after,
                     attachments=attachments, receiver=receiver)

    '''
        结果发钉钉机器人
    '''
    s = '#### 数据资源平台日常巡检指标\n' \
        '> ###### 播报时间: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +'&nbsp;&nbsp;&nbsp;指标情况 **[指标报表](https://www.dingtalk.com)** \n' \
        '*** \n' \
        '![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png) \n' \
        '--- \n' \
        '#### 整体事项监测情况 \n' \
        '#### <font color=#C0C0C0>总事项数          正常数         异常数 </font>\n' \
        '#### <font color=#C0C0C0>      20</font> <font color=#32CD32>          19</font> <font color=#FF0000>              <strong>1</strong> </font>\n' \
        '   \n'\
        '#### 监测事项一:数据库连通性监测 \n' \
        '#### <font color=#C0C0C0>总事项数          正常数         异常数 </font> \n' \
        '> <font color=#C0C0C0>      6</font> <font color=#32CD32>          5</font> <font color=#FF0000>              1</font>\n' \
        '###### 事项一列表 \n' \
        'db_name find_time orgin_value today_value if_normal\n'

    # for i in range(0,data1.shape[0]):
    #     s = s + '- '+data1.iloc[i]['db_name']+'|'+str(data1.iloc[i]['find_time'])+\
    #         '|'+str(data1.iloc[i]['orgin_value'])+ '|'+str(data1.iloc[i]['today_value'])+\
    #         '|'+str(data1.iloc[i]['if_normal'])+' \n'
    #
    # print(s)
    access_token = '266a461382aa24505a8720e29b78accf125c1313381f6cdbe8d595cd8eef45ab' # 创建webhook机器人时的access_token
    dt = dingtalk.DingTalk(access_token)
    title = '数据源检测test'
    text = s
    at_mobiles = ['18844058377']
    at_all = False
    response = dt.send_markdown(title, s, at_mobiles, at_all)
    print(response)
    '''
        结果大屏展示
    '''
    # c = (
    #     Pie()
    #         .add("",[list(z) for z in zip(data1.groupby(['if_normal'])['db_name'].count().index.to_list(),data1.groupby(['if_normal'])['db_name'].count().to_list())])
    #         .set_colors(["orange", "green", "yellow", "red", "pink", "orange", "purple"])
    #         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    #         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #         .render("pie_set_color.html")
    # )

    '''
        结果服务器列表展示
    '''

