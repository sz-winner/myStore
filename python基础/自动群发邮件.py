import smtplib, getpass, csv
from email.mime.text import MIMEText
from email.header import Header

# 发件人信息
sender = input('请输入发件人邮箱地址:')
smtp_server = 'smtp.exmail.qq.com'  # hotmail邮件服务器
smtp_port = 465
mail_psd = getpass.getpass('请输入您的邮箱密码：')

# 收件人信息
# 用CSV文件记录收件人，先写入收件人数据，当然也可以手工创建CSV文件
data = [['winner1 ', 'sz_winner@msn.com'], ['winner2', 'sz_winner@hotmail.com'],['lijh', '13688845032@139.com']]

with open('D:\\Python\\receivers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
# '''

# 定义邮件内容
# msg_text = input('请输入要发送的邮件内容：')
msg_text = '''Hello,Winner！
​    这是第12封python测试邮件。如果你所有的邮箱都收到了这封邮件，那么，祝贺你！
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
mail_msg = MIMEText(msg_text, 'plain', 'utf-8')

# 连接邮件发送服务
server = smtplib.SMTP_SSL(smtp_server)  # server = smtplib.SMTP_SSL() 当SMTP采用SSL加密时使用
server.connect(smtp_server, smtp_port)

# 登录邮箱
server.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
# server.starttls()  # 但若发件人为腾旭企业邮箱，在实际执行时会报错，屏蔽此语句后邮件发送正常
'''
Python发送邮件报如下错误，故加上上面这两行代码：
Traceback (most recent call last):
  File "d:/Python/myPython learning/myStore/自动发送邮件.py", line 19, in <module>
    server.login(sender, mail_psd)
smtplib.SMTPNotSupportedError: SMTP AUTH extension not supported by server.
'''
server.login(sender, mail_psd)

#发送邮件
with open('D:\\Python\\receivers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        receivers = row[1]
        mail_msg = MIMEText(msg_text, 'plain', 'utf-8')
        mail_msg['From'] = Header(sender)
        mail_msg['To'] = Header(receivers)
        mail_msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, smtp_port)
        server.login(sender, mail_psd)
        try:
            server.sendmail(sender, receivers, mail_msg.as_string())
            print('收件人：%s 邮件发送成功' % receivers)
        except:
            print('收件人%s发送失败' % receivers)

# 关闭邮箱服务
server.quit()
