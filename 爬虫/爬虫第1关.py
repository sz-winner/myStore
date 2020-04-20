import requests

res_h = requests.get(
    'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'
)

if res_h.status_code == 200:  # 先判断返回是否正确
    html_1 = res_h.text
with open('D:\\Python\\test\\test_html.html', 'a+', encoding='utf-8') as th:
    th.write(html_1)
for lines in open('D:\\Python\\test\\test_html.html', 'r', encoding='utf-8'):
    print(lines)
