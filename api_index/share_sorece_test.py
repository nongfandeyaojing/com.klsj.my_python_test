from docx.shared import Mm
from docxtpl import DocxTemplate,RichText,InlineImage
import time
from complite import data_to_email
import pandas as pd
from pydocx import PyDocX
from docx import Document


if __name__ == '__main__':

    '''
        结果word模板化
    '''
    # # 时间
    today = time.strftime("%Y-%m-%d", time.localtime())
    today_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 文件路径
    templa_doc_file = '2021.5.17海口市政务信息资源共享的工作报告模板.docx'  #模板路径
    day_doc_path = '海口市政务信息资源共享的工作报告' + today + '.docx' #每日存放路径
    # day_excel_path = 'resourse/日常监测每日excel/'  #每日监测excel存放路径
    # '''
    #         结果写入到word
    #     '''
    tpl = DocxTemplate(templa_doc_file)
    ri = RichText()

    # docx 富文本插入、样式设计
    context = {
            "zwxxgx_100101":  33,
            "zwxxgx_100102":690,
            "zwxxgx_100103": 27,
            "zwxxgx_100104": 38,
            "zwxxgx_100105":  11,
            "zwxxgx_100106":  4,
            "zwxxgx_100107":  7,
            "zwxxgx_100108": 30,
            "zwxxgx_100109":  508,
            "zwxxgx_100110":  29,
            "zwxxgx_100111":  614,
            "zwxxgx_100112":  9,
            "zwxxgx_100113":  1164,
            "zwxxgx_100114":  46,
            "zwxxgx_100115":  1378,
            "zwxxgx_100116":  729,
            "zwxxgx_100117":  245,
            "zwxxgx_100118":  24,
            "zwxxgx_100119":  222,
            "zwxxgx_100120":  115,
            "zwxxgx_100121":  72,
            "zwxxgx_100122":  503,
            "zwxxgx_100123":  216,
            "zwxxgx_100124":  10,
            "zwxxgx_100125":  75,
            "zwxxgx_100126":  42,
            "zwxxgx_100127":  23,
            "zwxxgx_100128":  19,
            "zwxxgx_100129":  10,
            "zwxxgx_100130":  998,
            "zwxxgx_100131":  99,
            "zwxxgx_100132":  5,
            "zwxxgx_100133":  4600,
            "zwxxgx_100134":  4,
            "zwxxgx_100135":  6,
            "zwxxgx_100136":  28,
            "zwxxgx_100137":  12,
            "zwxxgx_100138":  6,
            "zwxxgx_100139":  10,
            "zwxxgx_100140":  101,
            "zwxxgx_100141":  161,
            "zwxxgx_100142":  214
        }
    content1 = {
            "index_value": [33,	690,	27,	38,	11,	4,	7,	30,	508,	29,	614,	9,	1164,	46,	1378,	729,	245,	24,	222,	115,	72,	503,	216,	10,	75,	42,	23,	19,	10,	998,	99,	5,	4600,	4,	6,	28,	12,	6,	10,	101,	161,	214,],
             "index_id": ['zwxxgx_100101',	'zwxxgx_100102',	'zwxxgx_100103',	'zwxxgx_100104',	'zwxxgx_100105',	'zwxxgx_100106',	'zwxxgx_100107',	'zwxxgx_100108',	'zwxxgx_100109',	'zwxxgx_100110',	'zwxxgx_100111',	'zwxxgx_100112',	'zwxxgx_100113',	'zwxxgx_100114',	'zwxxgx_100115',	'zwxxgx_100116',	'zwxxgx_100117',	'zwxxgx_100118',	'zwxxgx_100119',	'zwxxgx_100120',	'zwxxgx_100121',	'zwxxgx_100122',	'zwxxgx_100123',	'zwxxgx_100124',	'zwxxgx_100125',	'zwxxgx_100126',	'zwxxgx_100127',	'zwxxgx_100128',	'zwxxgx_100129',	'zwxxgx_100130',	'zwxxgx_100131',	'zwxxgx_100132',	'zwxxgx_100133',	'zwxxgx_100134',	'zwxxgx_100135',	'zwxxgx_100136',	'zwxxgx_100137',	'zwxxgx_100138',	'zwxxgx_100139',	'zwxxgx_100140',	'zwxxgx_100141',	'zwxxgx_100142',],
            "index_comment": ['zwxxgx_100101',	'zwxxgx_100102',	'zwxxgx_100103',	'zwxxgx_100104',	'zwxxgx_100105',	'zwxxgx_100106',	'zwxxgx_100107',	'zwxxgx_100108',	'zwxxgx_100109',	'zwxxgx_100110',	'zwxxgx_100111',	'zwxxgx_100112',	'zwxxgx_100113',	'zwxxgx_100114',	'zwxxgx_100115',	'zwxxgx_100116',	'zwxxgx_100117',	'zwxxgx_100118',	'zwxxgx_100119',	'zwxxgx_100120',	'zwxxgx_100121',	'zwxxgx_100122',	'zwxxgx_100123',	'zwxxgx_100124',	'zwxxgx_100125',	'zwxxgx_100126',	'zwxxgx_100127',	'zwxxgx_100128',	'zwxxgx_100129',	'zwxxgx_100130',	'zwxxgx_100131',	'zwxxgx_100132',	'zwxxgx_100133',	'zwxxgx_100134',	'zwxxgx_100135',	'zwxxgx_100136',	'zwxxgx_100137',	'zwxxgx_100138',	'zwxxgx_100139',	'zwxxgx_100140',	'zwxxgx_100141',	'zwxxgx_100142',]

    }
    tpl.render(context)
    tpl.save(day_doc_path)

    '''
    word转html
    '''
    html = PyDocX.to_html("海口市政务信息资源共享的工作报告2021-06-16.docx")

    print(html)
    with open("海口市政务信息资源共享的工作报告2021-06-16.html", 'w',  encoding="utf-8") as f:
        f.write(html)

    '''
        结果发邮件
    '''
    smtp_server='smtp.qq.com'
    email_user='1601052583@qq.com'
    email_pass='qhpgorhoeqzsgaeh'
    email_port=25
    sender='1601052583@qq.com'
    receiver=["gm1-swws7xrmm@dingtalk.com"]
    html_head='''<!doctype html>
                <html><head>
                <meta charset="utf-8">
                <style type="text/css">
                .container {
                        width:100%;
                padding-right:15px;
                padding-left:15px;
                margin-right:auto;
                margin-left:auto
                }
                .table {
                        width:100%;
                margin-bottom:1rem;
                color:#212529
                }
                .table-striped tbody tr:nth-of-type(odd) {
                        background-color:rgba(0, 0, 0, .05)
                }
                .table td, .table th {
                        padding:.75rem;
                vertical-align:top;
                border-top:1px solid #dee2e6
                }
                </style>
                </head>
                <div class="container">'''
    html_after='</div></body><br/><br/><!doctype html>'
    d_t_e = data_to_email.Data_To_Email(smtp_server, email_user, email_pass, email_port)


    df_html1 = d_t_e.df_to_html(pd.DataFrame(content1))

    attachments = [
            {
                    "filepath": "海口市政务信息资源共享的工作报告"+today+".docx",
                    "filename": "海口市政务信息资源共享的工作报告"+today+".docx",
                    "email_type": ""
            }
    ]
    # d_t_e.send_Email(sender=sender, subject="海口市政务信息资源共享的工作报告", context_html=d_t_e.html_head+'<h2><img src="cid:0"></h2>'
    #                                                                    + '<h2>1.海口市政务信息资源共享的工作报告</h2>'+df_html1
    #
    #                                                                    + d_t_e.html_after,
    #                  attachments=attachments, receiver=receiver)
    d_t_e.send_Email(sender=sender, subject="【自动化】海口市政务信息资源共享的工作报告【测试】"+today, context_html=html,
                     attachments=attachments, receiver=receiver)
