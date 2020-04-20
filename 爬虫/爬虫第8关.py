'''
课堂练习：登录博客发表评论
'''
'''
实现方法一：使用cookies方法
'''
import requests
# 把请求登录的博客地址赋值给url
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 封装请求头，避开网站的反爬机制
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
# 把登录相关的参数封装成字典，赋值给data
log_data = {
    'log': 'spiderman',
    'pwd': 'crawler334566',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie':'1'
}
# 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in
login_in=requests.post(url,headers=headers,data=log_data)
# 调用requests对象的cookies属性提取登录用户的cookies，并赋值给变量log_cookies
log_cookies = login_in.cookies

# 我们想要发表评论的文章网址
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 把评论有关的参数封装成字典
data_1={'comment':input('请输入您要发表的评论：'),'submit':'发表评论','conmment_post_ID':'13','comment_parent':'0'}

comment = requests.post(url_1,
                        headers=headers,
                        data=data_1,
                        cookies=log_cookies)
print(comment.status_code)

'''
实现方法二：使用session方法
'''
import requests
# 创建session对象
session=requests.session()
# 把请求登录的博客地址赋值给url
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 封装请求头，避开网站的反爬机制
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
# 把登录相关的参数封装成字典，赋值给data
log_data = {
    'log': 'spiderman',
    'pwd': 'crawler334566',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
# 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in
session.post(url, headers=headers, data=log_data)

# 我们想要发表评论的文章网址
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 把评论有关的参数封装成字典
data_1 = {
    'comment': input('请输入您要发表的评论：'),
    'submit': '发表评论',
    'conmment_post_ID': '13',
    'comment_parent': '0'
}

comment = session.post(url_1, headers=headers, data=data_1)
print(comment.status_code)


'''
代码优化版：先读取本地cookie文件
'''
import requests, json
session = requests.session()
#创建会话。
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#添加请求头，避免被反爬虫。
try:
    #如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
    cookies_txt = open('cookies.txt', 'r')
    #以reader读取模式，打开名为cookies.txt的文件。
    cookies_dict = json.loads(cookies_txt.read())
    #调用json模块的loads函数，把字符串转成字典。
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    #把转成字典的cookies再转成cookies本来的格式。
    session.cookies = cookies
    #获取会话下的cookies

except FileNotFoundError:
    #如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。

    url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    #登录的网址。
    data = {
        'log': input('请输入你的账号:'),
        'pwd': input('请输入你的密码:'),
        'wp-submit': '登录',
        'redirect_to':
        'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': '1'
    }
    #登录的参数。
    session.post(url, headers=headers, data=data)
    #在会话下，用post发起登录请求。

    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #把cookies转化成字典。
    cookies_str = json.dumps(cookies_dict)
    #调用json模块的dump函数，把cookies从字典再转成字符串。
    f = open('cookies.txt', 'w')
    #创建名为cookies.txt的文件，以写入模式写入内容
    f.write(cookies_str)
    #把已经转成字符串的cookies写入文件
    f.close()
    #关闭文件

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
#文章的网址。
data_1 = {
    'comment': input('请输入你想评论的内容：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
#评论的参数。
session.post(url_1, headers=headers, data=data_1)
#在会话下，用post发起评论请求。


'''
终极优化版：把各个功能封装成函数
'''
import requests, json
session = requests.session()  # 创建会话
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 添加请求头，避开反爬机制


def cookies_read():  # 创建读取cookies的函数
    cookies_txt = open('cookies.txt', 'r')  # 以只读方式打开cookies文件
    cookies_dict = json.loads(cookies_txt.read())  # 调用json模块的loads函数，把字符串转换成字典
    cookies = requests.utils.cookiejar_from_dict(
        cookies_dict)  # 把字典格式的cookies转换成浏览器能识别的cookies
    return (cookies)


def sign_in():  # 创建登录博客的函数
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'  # 想要登录的网址
    data = {
        'log': input('请输入您的登录账号：'),
        'pwd': input('请输入您的登录密码：'),
        'wp-submit': '登录',
        'redirect_to':
        'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookies': '1'
    }  # 登录参数
    session.post(url, headers=headers, data=data)  # 在会话下，用post发起登录请求
    cookies_dict = requests.utils.dict_from_cookiejar(
        session.cookies)  # 把cookies转换成字典
    cookies_str = json.dumps(cookies_dict)  # 调用json模块的dump函数，把cookies从字典转换成字符串
    f = open('cookies.txt', 'w')  # 以写模式创建名为cookies.txt的文件
    f.write(cookies_str)  # 把字符串格式的cookies写入文件
    f.close()  # 关闭文件


def write_message():  # 创建发表评论的函数
    url_2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    #  要评论的博客的文章地址
    data_2 = {
        'comment': input('请输入您想评论的内容：'),
        'submit': '发表评论',
        'commnet_post_ID': '13',
        'comment_parent': '0'
    }  # 评论的参数
    return (session.post(url_2, headers=headers, data=data_2))


try:  # 执行cookies_read函数，尝试读取cookies
    session.cookies = cookies_read()
except FileNotFoundError:  # 如果读取不到，就执行登录函数
    sign_in()

num = write_message()
if num.status_code == 200:
    print('评论成功发表！')
else:
    sign_in()
    num = write_message()
