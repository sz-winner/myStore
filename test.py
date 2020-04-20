import requests, json
session = requests.session()  # 创建会话
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 添加请求头，避开反爬机制


def cookies_read():  # 创建读取cookies的函数
    cookies_txt = open('cookies.txt', 'r')  # 以只读方式打开cookies文件
    cookies_dict = json.loads(cookies_txt.read())  # 调用json模块的loads函数，把字符串转换成字典
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)  # 把字典格式的cookies转换成浏览器能识别的cookies
    return (cookies)


def sign_in():  # 创建登录博客的函数
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'  # 想要登录的网址
    data = {'log': input('请输入您的登录账号：'),
            'pwd': input('请输入您的登录密码：'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookies': '1'}  # 登录参数
    session.post(url, headers=headers, data=data)  # 在会话下，用post发起登录请求
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)  # 把cookies转换成字典
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
    return(session.post(url_2, headers=headers, data=data_2))


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
