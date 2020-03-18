import smtplib, getpass
from email.mime.text import MIMEText
from email.header import Header

# 发件人信息
sender = input('请输入发件人邮箱地址:')
smtp_server = 'smtp.exmail.qq.com'  # hotmail邮件服务器
smtp_port = 465
mail_psd = getpass.getpass('请输入您的邮箱密码：')

# 收件人信息
# receiver = input('请输入收件人邮箱地址:')
# receiver = 'sz_winner@hotmail.com' 单个收件人
receivers = ['sz_winner@hotmail.com', 'sz_winner@msn.com']
'''也可以用列表方式接收终端输入的邮箱地址
receivers = []
while True:
    a=input('请输入收件人邮箱：')
    #输入收件人邮箱
    receivers.append(a)
    #写入列表
    b=input('是否继续输入，n退出，任意键继续：')
    #询问是否继续输入
    if b == 'n':
        break
'''

# 定义邮件内容
# msg_text = input('请输入要发送的邮件内容：')
msg_text = '''Hello,Winner！
​    这是第7封测试python邮件。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
mail_msg = MIMEText(msg_text, 'plain', 'utf-8')

# 定义邮件头信息
mail_msg['From'] = Header(sender)
# mail_msg['To'] = Header(receiver)  单个收件人
mail_msg['To'] = Header(",".join(receivers))
mail_msg['Subject'] = Header('python test')

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
server.sendmail(sender, receivers, mail_msg.as_string())  # 发送邮件的语法：server.sendmail(from_addr, to_addr, msg.as_string())

# 关闭邮箱服务
server.quit()
