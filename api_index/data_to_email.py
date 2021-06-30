import email,smtplib
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base        import MIMEBase
from email.mime.multipart   import MIMEMultipart
import  pandas as pd

import re

class Data_To_Email:

    def __init__(self,smtp_server, email_user, email_pass, email_port):
        """
            发送邮件服务器、邮箱账号、SMTP服务密码、邮件服务器端口
        """
        self.smtp_server = smtp_server
        self.email_user = email_user
        self.email_pass = email_pass
        self.email_port = email_port
        self.msg = MIMEMultipart()
        self.html_head = '''
                            <!doctype html>
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
                                  <div class="container">
                            '''
        self.html_after = '</div></body><br/><br/><!doctype html>'

    def df_to_html(self, df):
        df_html = re.sub(u'<tr style="text-align: right;">', u'<tr>', re.sub(u'<table border="1" class="dataframe">', u'<table class="table table-striped">', df.to_html(index=False)))
        return df_html

    def send_Email(self, sender, subject, context_html, attachments=[], receiver=[]  ):
        """
            发件人、收件人信息
        """
        sender = sender
        receiver = receiver

        """
            信息封装
        """
        self.msg["subject"] = Header(subject)
        self.msg["from"] = formataddr((Header("刘宝盛QQ", "utf-8").encode(), sender))
        self.msg["to"] = formataddr((Header("刘宝盛钉钉", "utf-8").encode(), receiver[0]))

        context_html1 = MIMEText(context_html, "html", "utf-8")

        # 添加附件到包装对象中
        self.msg.attach(context_html1)


        for i in attachments:

            if i['email_type'] == 'image':
                attachment = MIMEImage(open(i['filepath'], 'rb').read())
                attachment.add_header("Content-Disposition", "attachment", filename=i['filename'])
                attachment.add_header('Content-ID', '<'+i['id']+'>')

            else:
                attachment = MIMEApplication(open(i['filepath'],'rb').read())
                attachment.add_header("Content-Disposition", "attachment", filename=i['filename'])

            # 添加附件到包装对象中
            self.msg.attach(attachment)

        """
            连接邮件服务器、用户登录、发送邮件、退出
        """
        server = smtplib.SMTP_SSL(self.smtp_server, 465)
        server.login(self.email_user, self.email_pass)
        server.sendmail(sender, receiver, self.msg.as_string())
        server.quit();
        print("邮件发送结束")











