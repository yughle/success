#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 21:52
# @Author  : yuzhenyu
# @File    : send_email.py
import smtplib
from email.mime.text import MIMEText


def send():
    smtpserver="smtp.qq.com"
    user="895995165@qq.com"
    password="upuzyjeagynkbbfj"
    #发送邮箱
    sender="895995165@qq.com"
    #接收邮箱
    receiver="895995165@qq.com"
    #邮件正文
    msg=MIMEText("测试1236")
    msg["subject"]="测试666666"
    msg["from"]=sender
    msg["to"]=receiver
    #连接发送邮件
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

send()


