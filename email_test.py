import email,smtplib
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base        import MIMEBase
from email.mime.multipart   import MIMEMultipart

from email                  import encoders

"""
    发送邮件服务器、邮箱账号、SMTP服务密码、邮件服务器端口
"""
smtp_server = "smtp.qq.com"
email_user = "1601052583@qq.com"
email_pass = "qhpgorhoeqzsgaeh"
email_port = 25

msgtype = "mul"
"""
    发件人、收件人信息
"""
sender = email_user
receiver = ["gm1-swws7xrmm@dingtalk.com"]


"""
    信息封装
"""
html_s = '<table id="table-fq1-cza-tif" class="table"><colgroup colnum="1" colname="col1" colwidth="1*" id="colgroup-570-okz-ys2" style="width:20%"></colgroup><colgroup colnum="2" colname="col2" colwidth="1*" id="colgroup-hn1-atd-n7n" style="width:20%"></colgroup><colgroup colnum="3" colname="col3" colwidth="3*" id="colgroup-2vg-i98-s36" style="width:60%"></colgroup><thead id="thead-ian-8hp-laa" class="thead"><tr id="tr-ugq-jic-yev"><th id="td-ck8-bj2-f1p"><p id="p-e4y-6vj-vav">开发者</p></th><th id="td-t99-w01-sz0"><p id="p-0va-p48-u4h">开发的应用类型</p></th><th id="td-3h4-6t1-47i"><p id="p-pqx-7gx-xio">关联的组织</p></th></tr></thead><tbody id="tbody-nmn-b5x-tw0" class="tbody"><tr id="tr-cr4-4lg-h31"><td id="td-9w3-kfi-3eu"><p id="p-965-7gs-frv">应用服务商的开发者</p></td><td id="td-yqi-5xs-5jf"><p id="p-nls-412-joq">第三方企业应用</p></td><td id="td-mu0-z88-pvb"><p id="p-a1b-27z-y48">作为应用服务商的开发者开发第三方企业应用，你的企业组织必须完成应用服务商认证。详情请参考<a href="https://ding-doc.dingtalk.com/document/operation-specification/joinPROCESS?pnamespace=app" id="a-i4g-tbh-mag" data-tag="xref" baseurl="" class="xref" target="_blank">应用服务商入驻流程</a>。</p></td></tr><tr id="tr-r6f-mfh-80s"><td id="td-yk6-u8k-lea"><p id="p-mil-aff-yty" data-spm-anchor-id="ding_open_doc.document.0.i10.6d9d28e1N7rWYs">定制服务商的开发者</p></td><td id="td-a7n-d7r-nm4"><p id="p-vp9-uh9-bfa">以委托身份开发企业内部应用</p></td><td id="td-oe7-0mz-ar1"><p id="p-dnn-gv8-klx" data-spm-anchor-id="ding_open_doc.document.0.i12.6d9d28e1N7rWYs">作为定制服务商的开发者为企业定制开发应用，你的企业组织必须完成定制服务商认证。详情请参考<a href="https://ding-doc.dingtalk.com/document/operation-specification/become-a-si-partner?pnamespace=app" id="a-rdi-yw4-40l" data-tag="xref" baseurl="" class="xref" target="_blank">定制服务商商入驻流程</a>。</p></td></tr><tr id="tr-8g4-bkk-z6g"><td id="td-h01-6kv-6oa"><p id="p-d0b-lj3-ubh">企业内部开发者</p></td><td id="td-b3y-5oq-yo5"><p id="p-zy6-fcw-7ot">企业自建内部应用</p></td><td id="td-is3-x6a-kbh"><p id="p-eaw-5gs-ka3">作为企业内部员工开发企业自建应用，你的企业组织必须完成企业认证。</p></td></tr></tbody></table>'
html_s1 = '''
<table width="100%" border-collapse="collapse" margin="0 auto" text-align="center" border=1>
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody >
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>john@example.com</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>mary@example.com</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>july@example.com</td>
      </tr>
    </tbody>
  </table>
'''
msg = MIMEMultipart()
# 传入基本信息
msg["subject"] = Header("test来自刘宝盛qq的问候")
# msg["from"] = _format_addr("刘宝盛 <%s>" % sender)
msg["from"] = formataddr((Header("刘宝盛qq", "utf-8").encode(), email_user))
msg["to"] = formataddr((Header("刘宝盛钉钉", "utf-8").encode(), receiver[0]))

if msgtype == 'text':
    # 发送的消息设置，plain表示文本，utf-8表示数据编码格式,
    content  = MIMEText("这是一个自动发送的邮件", "plain", "utf-8")
    msg.attach(content)

if msgtype == 'html':
    # 发送的消息设置，html页面模式，支持表格，utf-8表示数据编码格式,
    content  = MIMEText(html_s, "html", "utf-8")
    msg.attach(content)


if msgtype == 'mul':

    # Text和html只能存在一个
    # content_text  = MIMEText("这是一个自动发送的邮件", "plain", "utf-8")
    # 图片只能通过MIMEImage设置。'Content-ID','<image1>'
    # https://www.jb51.net/article/203433.htm
    content_html_pic  = MIMEText('<h2>这是邮件正文内容部分<img src="cid:0"></h2>', "html", "utf-8")
    attachment_pic = MIMEApplication(open("邮件测试图片.jpg",'rb').read())
    attachment_image = MIMEImage(open("邮件测试图片.jpg",'rb').read())
    attachment_file = MIMEApplication(open("dingtalk_test.py",'rb').read())
    attachment_zip = MIMEApplication(open("dingtalk_test.zip",'rb').read())
    # 设置附件信息
    attachment_pic.add_header("Content-Disposition", "attachment", filename="邮件测试图片.jpg")

    attachment_image.add_header("Content-Disposition", "attachment", filename="邮件正文测试图片.jpg")
    attachment_image.add_header('Content-ID','<0>')

    attachment_file.add_header("Content-Disposition", "attachment", filename="dingtalk_test.py")
    attachment_zip.add_header("Content-Disposition", "attachment", filename="dingtalk_test.zip")

    # 添加附件到包装对象中

    msg.attach(content_html_pic)
    msg.attach(attachment_image)
    msg.attach(attachment_pic)
    msg.attach(attachment_file)
    msg.attach(attachment_zip)

else:
    print('请输入正确的msgtype类型')



"""
    连接邮件服务器、用户登录、发送邮件、退出
"""
server = smtplib.SMTP_SSL(smtp_server, 465)
server.login(email_user, email_pass)
server.sendmail(sender, receiver, msg.as_string())
server.quit();
print("邮件发送结束")


