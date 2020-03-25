 -*- coding: UTF-8 -*-
import smtplib, ssl, getpass # 定義一個簡單的 SMTP 客戶端，可以用來發送信
from email.mime.text import MIMEText # 文本郵件對象
from email.mime.image import MIMEImage # 作為附件的圖片
from email.header import Header
from dotenv import load_dotenv
load_dotenv()

# 用讀檔的方式

sender = 'xiaoClassmate who is the Greatest' # 送件者
receivers = [
    'myg36t91@gmail.com'
] # 收件者
subject = 'Python SMTP 的測試' # 主題
body = '考試終於考了100分，..............，考多益' # 內容
password = getpass.getpass("Type your password and press enter: ")
context = ssl.create_default_context() # 返回帶有安全默認設置的上下文
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] =  Header(sender, 'utf-8')
msg['To'] = Header('xiaoClassmate', 'utf-8')

server = smtplib.SMTP(host='smtp.gmail.com', port=587)
try:
    server.ehlo()
    server.starttls(context=context)  # starttls 把已經存在的一條不安全的連結, 用SSL/TLS的加密方法, 升級成安全的連接
    server.login('yuyixaio@gmail.com', password)
    server.sendmail(sender, receivers, msg.as_string())
    print('Success')
except smtplib.SMTPException as E:
    print(E)
finally:
    server.quit()