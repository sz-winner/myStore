import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

fp = open("D:\\Python\\test_mail.eml", "r")
msg = email.message_from_file(fp)  # 直接文件创建message对象，这个时候也会做初步的解码
subject = msg.get("subject")  # 取信件头里的subject,也就是主题

# 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
h = email.Header.Header(subject)
dh = email.Header.decode_header(h)
subject = dh[0][0]

print("subject:", subject)
print("from: ", email.utils.parseaddr(msg.get("from"))[1])  # 取from
print("to: ", email.utils.parseaddr(msg.get("to"))[1])  # 取to

# 循环信件中的每一个mime的数据块，获取邮件内容
for par in msg.walk():
    if not par.is_multipart():  # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
        name = par.get_param("name")  # 如果是附件，这里就会取出附件的文件名
        if name:
            # 有附件
            # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
            h = email.Header.Header(name)
            dh = email.Header.decode_header(h)
            fname = dh[0][0]
            print('附件名:', fname)
            data = par.get_payload(decode=True)  # 解码出附件数据，然后存储到文件中
            try:
                f = open(fname, 'wb')  # 注意一定要用wb来打开文件，因为附件一般都是二进制文件
            except:
                print('附件名有非法字符，自动换一个')
                f = open('aaaa', 'wb')
            f.write(data)
            f.close()
        else:
            # 不是附件，是文本内容
            print(par.get_payload(decode=True))  # 解码出文本内容，直接输出来就可以了。
        print('+' * 60)  # 用来区别各个部分的输出
