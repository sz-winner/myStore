'''
练习一：去下厨房网站（http://www.xiachufang.com/explore/）爬取热门菜谱清单，内含：菜名、原材料、详细烹饪流程的URL
注意：.text方法可以提取的包括子标签内的所有文本内容
'''
import requests
from bs4 import BeautifulSoup

res_1 = requests.get('http://www.xiachufang.com/explore/')
html_1 = res_1.text
soup_1 = BeautifulSoup(html_1, 'html.parser')
items_1 = soup_1.find_all('div', class_='info pure-u')
print(items_1)
for item_1 in items_1:
    recipe_name = item_1.find('a')
    recipe_ing = item_1.find('p', class_='ing ellipsis')
    print('【菜谱名:' + ((recipe_name.text).strip()) + '】', '\n【菜单构成】' + recipe_ing.text,
        'http://www.xiachufang.com' + recipe_name['href'])  # 爬取菜单名、详情链接 Ok
    print('')

'''
# 以下为教材内答案
# 方法一：先去爬取所有的最小父级标签<div class="info pure-u">，然后针对每一个父级标签，想办法提取里面的菜名、URL、食材。
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 查找最小父级标签
list_foods = bs_foods.find_all('div',class_='info pure-u')

# 创建一个空列表，用于存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('a')
    # 菜名，使用[17:-13]切掉了多余的信息
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com'+tag_a['href']
    # 提取第0个父级标签中的<p>标签
    tag_p = food.find('p',class_='ing ellipsis')
    # 食材，使用[1:-1]切掉了多余的信息
    ingredients = tag_p.text[1:-1]
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name,URL,ingredients])

# 打印
print(list_all)

# 方法二：分别提取所有的菜名、所有的URL、所有的食材。然后让菜名、URL、食材给一一对应起来。
# 查找所有，包含菜名和URL的<p>标签。此处<p>标签是<a>标签的父标签。
# 为什么不直接选<a>标签？在实践操作当中，其实常常会因为标签选取不当，或者网页本身的编写没做好板块区分，可能会多打印出一些奇怪的东西。
# 当遇到这种糟糕的情况，一般有两种处理方案：数量太多而无规律，可以换个标签提取；数量不多而有规律，
# 我们会对提取的结果进行筛选——只要列表中的若干个元素就好。这里如果是直接提取<a>标签，就会遇到这种情况。
# 去查找所有包含食材的<p>标签，创建一个空列表，启动循环，循环长度等于<p>标签的总数——可以借助range(len())语法。
# 在每一次的循环里，去提取一份菜名、URL、食材。拼接为小列表，小列表拼接成大列表。输出打印。

# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

# 查找包含菜名和URL的<p>标签
tag_name = bs_foods.find_all('p',class_='name')
# 查找包含食材的<p>标签
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# 创建一个空列表，用于存储信息
list_all = []
# 启动一个循环，次数等于菜名的数量
for x in range(len(tag_name)):
    # 提取信息，封装为列表。注意下面[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    # 将信息添加进 list_all
    list_all.append(list_food)
# 打印
print(list_all)
'''

'''
练习二、把豆瓣TOP250里面的 序号/电影名/评分/推荐语/链接 都爬取下来，结果就是全部展示打印出来
分析：豆瓣电影是通过HTML来处理排行榜的，top250的网址如下：
https://movie.douban.com/top250?start=0&filter=
变量在start，第1页start=0，第2页start=25，第3页start=50，以此类推。因此，可通过设计一个循环来翻页爬取数据
'''
import requests, bs4
# 为躲避反爬机制，伪装成浏览器的请求头
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

for x in range(10):  # 设计一个循环，逐页爬取
    movies_url = 'https://movie.douban.com/top250?start=' + str(
        x * 25) + '&filter='  # 获取每一页的链接地址
    movies_res = requests.get(movies_url, headers=headers)
    movies_html = movies_res.text
    movies_soup = bs4.BeautifulSoup(movies_html, 'html.parser')
    movies_list = movies_soup.find('ol', class_='grid_view').find_all('li')
    for list in movies_list:
        num = list.find('em', class_='').text  # 爬取序号
        name = list.find('span', class_='title').text  # 爬取电影名
        score = list.find('span', class_='rating_num').text  # 爬取评分
        # 因为存在没有评语的情况，此时要做例外处理
        try:
            comment = list.find('span', class_='inq').text  # 爬取评语
        except AttributeError:
            comment = '此电影没有评语'  # 如果用pass的话，python会用上一条记录的内容替代，所以此处强制写内容
        movie_url = list.find('a')['href']  # 爬取链接
        print('【第{}名】【{}】【得分：{}】【评语：{}】 观看请点击 {}'.format(
            num, name, score, comment, movie_url))

'''
练习三（未完成）、输入喜欢的电影名字，然后在电影天堂https://www.ygdy8.com爬取电影所对应的下载链接，并将下载链接打印出来。
步骤：
1. 输入对话框，提示用户输入想要搜索的电影/电视剧名称
2. 用encode('gbk')将输入的中文电影名称解析成utf-8格式
3. 拼接网址
'''
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
film_name = input('请输入您想要下载的电影名：')
film_code = film_name.encode('gbk')  # 将输入的电影名称转换成16进制码
urllib.request.quote(film_code)  # 将上面转换的16进制码转换成url格式


'''
课外练习：在日本传统色彩大全网页上(http://wenliku.com/ribense.html)，提取颜色名称和色码
'''
# 方法一，用风变课程教授的方法
import requests
from bs4 import BeautifulSoup
url = 'http://wenliku.com/ribense.html'  #爬取网页所在网页
res = requests.get(url)
print(res.status_code)  #根据码，判断网页能否爬取
res.encoding = 'utf-8'  #确保以utf-8编码格式展示
soup = BeautifulSoup(res.text, 'html.parser')  #把html代码转化成BeautifulSoup能看得懂的
# 把res解析为字符串
cnames = soup.find(class_="container clearfix").find_all(
    "a")  #所需要的数据在这个类,所有的颜色都在a标签内
for cname in cnames:  #find_all()的数据类似是列表排列，用遍历列表的方式把每个元素提取出来。
    print(cname.text + '\n')  #只要内容部分，标签不要

# 方法二，用xpath
import requests
from lxml import etree
url = 'http://wenliku.com/ribense.html'  # 爬取网页所在网页
res = requests.get(url)
res.encoding = 'utf-8'
html = etree.HTML(res.text)
result_data = html.xpath('/html/body/div[2]//ul/li/a')  # 写
result_code = html.xpath('/html/body/div[2]//ul/li/a/span')  # 写
for i in result_data:
    print(i.text)
for j in result_code:
    print(j.text)