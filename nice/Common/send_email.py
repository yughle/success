#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 21:52
# @Author  : yuzhenyu
# @File    : send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



def send():
    smtpserver="smtp.qq.com"
    user="xxx@qq.com"
    password=""
    #发送邮箱
    sender="xxx@qq.com"
    #接收邮箱
    receiver="xxx@qq.com"
    #邮件正文
    subject = 'Python SMTP 邮件测试'
    mail_msg = """
    链接
    """
    msg= MIMEText(mail_msg, 'html', 'utf-8')
    msg["subject"]="测试666666"
    msg["from"]=sender
    msg["to"]=receiver
    #连接发送邮件
    try:
        smtp=smtplib.SMTP_SSL(smtpserver,465)
        smtp.login(user,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print("发送失败")
        raise e
        open()