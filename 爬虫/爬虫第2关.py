import requests
from bs4 import BeautifulSoup

'''
BeautifulSoup网页解析语法：
from bs4 import BeautifulSoup
soup = BeautifulSoup(字符串,'html.parser')  # 注意第二个参数是固定值 html.parser
'''
'''
练习一：
以网站这个书苑不太冷为例：
（url：https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html），
目标是爬取网页中的三本书的书名、链接、和书籍介绍。
'''

# 第1步：获取网页资源，赋值给变量res
res_1 = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 第2步：将变量res的值解析成字符串，赋值给变量html
html_1 = res_1.text
# 第3步：用html解析器将变量html的值解析成text文件格式，赋值给变量soup
soup_1 = BeautifulSoup(html_1, 'html.parser')
# 第4步：根据项目要求，从变量soup中提取相关元素（此处是class_ = 'books'）
items_1 = soup_1.find_all(class_='books')
# 遍历列表items
for item_1 in items_1:
    # 在列表中的每个元素里，匹配标签h2，提取相关值给到变量kind
    kind = item_1.find('h2')
    # 在列表中的每个元素里，匹配属性class_='title'，提取相关值给到变量title
    title = item_1.find(class_='title')
    # 在列表中的每个元素里，匹配属性class_='info'，提取相关值给到变量brief
    brief = item_1.find(class_='info')
    # 打印书籍的类型、名字、链接和简介的文字
    # print(type(kind), type(title), type(brief))
    print(kind.text, '\n', title.text, '\n', title['href'], '\n', brief.text, '\n')

'''
练习二：爬取博客【人人都是蜘蛛侠】（https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/）中，
《未来已来（四）——Python学习进阶图谱》文章的默认评论页，并且打印。
'''

# 第1步：用requests.get方法获取网页数据
res_blog = requests.get(
    'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/comment-page-1128/#comments'
)
# # 第2步：用bs.text方法将第1步获取的网页数据转换成字符串
html_blog = res_blog.text
# # 第3步：用html.parser解析器将第2步获取的字符串转换成html格式化数据
soup_blog = BeautifulSoup(html_blog, 'html.parser')
items = soup_blog.find('ol', class_='comment-list').find_all(
    'p')  # 标签为ol，属性为comment-list的段中寻找p段
# print(items)
for item in items:
    content = item.text
    print(content)


'''
练习三：爬取网上书店Books to Scrape（http://books.toscrape.com/）中的一些信息:
1. 爬取网上书店Books to Scrape中所有书的分类类型，并且将它们打印出来。
2. 爬取首页（http://books.toscrape.com/catalogue/category/books/travel_2/index.html）的书名、评分、价格，并且打印出来。
目的：
1. 练习获取网页源代码，然后使用BeautifulSoup解析提取数据。
2. 强化训练find与find_all的用法。
3. 强化训练Tag的方法和属性。
'''

'''
1. 爬取图书分类
'''
res_1 = requests.get('http://books.toscrape.com')
html_1 = res_1.text
soup_1 = BeautifulSoup(html_1, 'html.parser')

items_1 = soup_1.find('ul', class_='nav nav-list').find_all('li')
for item_1 in items_1:
    print(item_1.find('a').text)

'''
2. 爬取首页（http://books.toscrape.com/catalogue/category/books/travel_2/index.html）的书名、评分、价格
'''
res_2 = requests.get(
    'http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html_2 = res_2.text
soup_2 = BeautifulSoup(html_2, 'html.parser')

items_2 = soup_2.find_all(class_='product_pod')
for item_2 in items_2:
    book_name = item_2.find('h3').find('a')  # 爬取书名已OK
    book_price = item_2.find('p', class_='price_color')  # 爬取价格已OK
    book_star = item_2.find('p', class_='star-rating')  # 爬取评分
    print('【书名】：%s；【价格】：%s；【评分】：%s Star' %
          (book_name.text, book_price.text, book_star['class'][1]))
'''
# 以下为助教提供的代码
res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
list_books = bs_bookstore.find_all(class_='product_pod')
for tag_books in list_books:
    tag_name = tag_books.find('h3').find('a') # 找到a标签需要提取两次
    list_star = tag_books.find('p',class_="star-rating")
    # 这个p标签的class属性有两种："star-rating"，以及具体的几星比如"Two"。我们选择所有书都有的class属性："star-rating"
    tag_price = tag_books.find('p',class_="price_color") # 价格比较好找，根据属性提取，或者标签与属性一起都可以
    print(tag_name['title']) # 这里用到了tag['属性名']提取属性值
    print('star-rating:',list_star['class'][1])
    # 同样是用属性名提取属性值
    # 用list_star['class']提取出来之后是一个由两个值组成的列表，如："['star-rating', 'Two']"，我们最终要提取的是这个列表的第1个值："Two"。
    # 为什么是列表呢？因为这里的class属性有两个值。其实，在这个过程中，我们是使用class属性的第一个值提取出了第二个值。
    print('Price:',tag_price.text, end='\n'+'------'+'\n') # 打印的时候，我加上了换行，为了让数据更加清晰地分隔开，当然你也可以不加。
'''

'''
3. 爬取博客【人人都是蜘蛛侠】首页(https://wordpress-edu-3autumn.localprod.oc.forchange.cn/)
的四篇文章标题、发布时间、文章链接，并且在终端打印提取到的信息。
'''
res_3 = requests.get(
    'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
html_3 = res_3.text
soup_3 = BeautifulSoup(html_3, 'html.parser')
items_3 = soup_3.find(class_='site-main').find_all('article')  # 要找两级，否则下面的循环只能找到一条记录
for item_3 in items_3:
    book_title = item_3.find(class_='entry-title')  # 爬取文章标题，OK
    book_time = item_3.find(class_='entry-date')  # 爬取文章时间
    book_link = item_3.find('a')  # 爬取文章链接，OK
    print('【%s】【发布时间：%s】：' % (book_title.text, book_time.text), book_link['href'])
