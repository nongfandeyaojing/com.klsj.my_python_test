# pyecharts依赖
from pyecharts.render import make_snapshot
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar,Line
from snapshot_selenium import snapshot
from pyecharts import options as opts
# 导入输出图片工具
from pyecharts.render import make_snapshot
from pyecharts.commons.utils import JsCode
from api_index import data_to_email

# docx模板依赖
from docxtpl import DocxTemplate,RichText,InlineImage
from docx.shared import Mm
# docx 转html工具
from pydocx import PyDocX

# mysql依赖
import pymysql

# 结构数，用来字符串转json
from ast import literal_eval
import json

# 日期
import datetime
import time
class MysqlUtil:
    def __init__(self, host, port, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, use_unicode=True, charset="utf8")

    def get_data(self, sql_content):
        cursor = self.conn.cursor()
        cursor.execute(sql_content)
        datas = cursor.fetchall()
        title = cursor.description
        cursor.close()
        if len(datas)==0:
            datas = (('',),)
        return(datas)

if __name__ == '__main__':

    # mysql配置信息
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = 'aptx4869'
    db = 'mybatis'
    sql_content = 'select index_value from sjzypt_monitor_index_tb where index_id = %s'
    mysqlUtil = MysqlUtil(host, port, user, password, db)

    # 基本信息
    c_day = mysqlUtil.get_data( sql_content%('100104'))[0][0]

    # 文件路径
    report_name = '海口市政务信息资源共享的工作报告'
    templa_doc_file = '2021.5.17'+report_name+'模板.docx'  #模板路径
    day_doc_path = report_name + mysqlUtil.get_data( sql_content%('100104'))[0][0] + '.docx' #每日监测文档存放路径
    # day_excel_path = 'resourse/日常监测每日excel/'  #每日监测excel存放路径

    '''
        结果word模板化
    '''
    tpl = DocxTemplate(templa_doc_file)
    ri = RichText()

    # docx 富文本插入、样式设计
    context = {
        'zwxxgx_100201': mysqlUtil.get_data( sql_content%('100201'))[0][0],
        'zwxxgx_100202': mysqlUtil.get_data( sql_content%('100202'))[0][0],
        'zwxxgx_100203': mysqlUtil.get_data( sql_content%('100203'))[0][0],
        'zwxxgx_100204': mysqlUtil.get_data( sql_content%('100204'))[0][0],
        'zwxxgx_100205': mysqlUtil.get_data( sql_content%('100205'))[0][0],
        'zwxxgx_100206': mysqlUtil.get_data( sql_content%('100206'))[0][0],
        'zwxxgx_100207': mysqlUtil.get_data( sql_content%('100207'))[0][0],
        'zwxxgx_100208': mysqlUtil.get_data( sql_content%('100208'))[0][0],
        'zwxxgx_100209': mysqlUtil.get_data( sql_content%('100209'))[0][0],
        'zwxxgx_100210': mysqlUtil.get_data( sql_content%('100210'))[0][0],
        'zwxxgx_100211': mysqlUtil.get_data( sql_content%('100211'))[0][0],
        'zwxxgx_100212': mysqlUtil.get_data( sql_content%('100212'))[0][0],
        'zwxxgx_100213': mysqlUtil.get_data( sql_content%('100213'))[0][0],
        'zwxxgx_100214': mysqlUtil.get_data( sql_content%('100214'))[0][0],
        'zwxxgx_100215': mysqlUtil.get_data( sql_content%('100215'))[0][0],
        'zwxxgx_100216': mysqlUtil.get_data( sql_content%('100216'))[0][0],
        'zwxxgx_100217': mysqlUtil.get_data( sql_content%('100217'))[0][0],
        'zwxxgx_100218': mysqlUtil.get_data( sql_content%('100218'))[0][0],
        'zwxxgx_100219': mysqlUtil.get_data( sql_content%('100219'))[0][0],
        'zwxxgx_100220': mysqlUtil.get_data( sql_content%('100220'))[0][0],
        'zwxxgx_100221': mysqlUtil.get_data( sql_content%('100221'))[0][0],
        'zwxxgx_100222': mysqlUtil.get_data( sql_content%('100222'))[0][0],
        'zwxxgx_100223': mysqlUtil.get_data( sql_content%('100223'))[0][0],
        'zwxxgx_100224': mysqlUtil.get_data( sql_content%('100224'))[0][0],
        'zwxxgx_100225': mysqlUtil.get_data( sql_content%('100225'))[0][0],
        'zwxxgx_100226': mysqlUtil.get_data( sql_content%('100226'))[0][0],
        'zwxxgx_100227': mysqlUtil.get_data( sql_content%('100227'))[0][0],
        'zwxxgx_100228': mysqlUtil.get_data( sql_content%('100228'))[0][0],
        'zwxxgx_100229': mysqlUtil.get_data( sql_content%('100229'))[0][0],
        'zwxxgx_100230': mysqlUtil.get_data( sql_content%('100230'))[0][0],
        'zwxxgx_100231': mysqlUtil.get_data( sql_content%('100231'))[0][0],
        'zwxxgx_100232': mysqlUtil.get_data( sql_content%('100232'))[0][0],
        'zwxxgx_100233': mysqlUtil.get_data( sql_content%('100233'))[0][0],
        'zwxxgx_100234': mysqlUtil.get_data( sql_content%('100234'))[0][0],
        'zwxxgx_100235': mysqlUtil.get_data( sql_content%('100235'))[0][0],
        'zwxxgx_100236': mysqlUtil.get_data( sql_content%('100236'))[0][0],
        'zwxxgx_100237': mysqlUtil.get_data( sql_content%('100237'))[0][0],
        'zwxxgx_100238': mysqlUtil.get_data( sql_content%('100238'))[0][0],
        'zwxxgx_100239': mysqlUtil.get_data( sql_content%('100239'))[0][0],
        'zwxxgx_100240': mysqlUtil.get_data( sql_content%('100240'))[0][0],
        'zwxxgx_100241': mysqlUtil.get_data( sql_content%('100241'))[0][0],
        'zwxxgx_100242': mysqlUtil.get_data( sql_content%('100242'))[0][0],
    }

    tpl.render(context)
    tpl.save(day_doc_path)

    '''
    word转html
    '''
    html = PyDocX.to_html(day_doc_path)
    #
    # with open("海口市政务信息资源共享的工作报告2021-06-16.html", 'w',  encoding="utf-8") as f:
    #     f.write(html)

    '''
        结果发邮件
    '''
    smtp_server='smtp.qq.com'
    email_user='1601052583@qq.com'
    email_pass='qhpgorhoeqzsgaeh'
    email_port=25
    sender='1601052583@qq.com'
    receiver=["gm1-swws7xrmm@dingtalk.com"]
    d_t_e = data_to_email.Data_To_Email(smtp_server, email_user, email_pass, email_port)


    # df_html1 = d_t_e.df_to_html(pd.DataFrame(content1))

    attachments = [
        {
            "filepath": day_doc_path,
            "filename": day_doc_path,
            "email_type": ""
        }
    ]
    d_t_e.send_Email(sender=sender,
                     subject="【自动化】" + report_name + "【测试】"+c_day,
                     context_html=html,
                     attachments=attachments, receiver=receiver)
