'''
课堂练习：爬取知乎大v张佳玮的文章“标题”、“摘要”、“链接”，并存储到本地csv文件。
'''
import requests
import csv

csv_file = open('D:\\Python\\test\\articles.csv',
                'w',
                newline='',
                encoding='gbk')
writer = csv.writer(csv_file)
list2 = ['标题', '链接', '摘要']
writer.writerow(list2)
zjw_headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

zjw_url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
articlelist = []  # 创建一个空列表，用来存放查询结果

offset = 10  # 设置起始页的offset值

while True:
    zjw_params = {'include': 'data[*].comment_count, suggest_edit, is_normal,thumbnail_extra_info,thumbnail,can_comment,\
        comment_permission, admin_closed_comment, content, voteup_count, created, updated, upvoted_followees, voting,\
        review_info,is_labeled, label_info; data[*].author.badge[?(type=best_answerer)].topics',
        'offset': str(offset), 
        'limit': '10', 
        'sort_by': 'voteups',}
    zjw_res = requests.get(zjw_url, headers=zjw_headers, params=zjw_params)  # 获取网页内容
    if int(zjw_res.status_code) == 200:  # 判断状态是否正常
        zjw_articles = zjw_res.json()  # 用json()方法解析respones对象
        zjw_data = zjw_articles['data']  # 定位并提取目标数据

        for i in zjw_data:
            list1 = [i['title'], i['url'], i['excerpt']]  # 将目标数据封装成类别
            writer.writerow(list1)
        offset = offset + 20
        # if articles['paging']['is_end'] == True:  # 当爬全部标题时可以用这个条件结束循环
        if offset > 100:
            break
csv_file.close()
print('爬虫结束工作！')
