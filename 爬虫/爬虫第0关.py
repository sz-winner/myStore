import requests

res_t = requests.get(
    'https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md'
)

text_1 = res_t.text

with open('D:\\Python\\test\\sanguo.txt', 'a+', encoding='utf-8') as tf:
    tf.write(text_1)

# 下面这两行代码是直接在终端逐行输出文本内容
for lines in open('D:\\Python\\test\\sanguo.txt', encoding='utf-8'):
    print(lines)

# 发出请求，并把返回的结果放在Response对象变量res_p中
res_p = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')

# 打印变量res的响应状态码，以检查请求是否成功
print(res_p.status_code)

# 把Reponse对象的内容以二进制数据的形式返回给变量pic
pic = res_p.content

# 新建一个文件并打开，然后将变量pic的内容写入该文件
with open('D:\\Python\\test\\test_photo.png', 'wb') as tp:
    tp.write(pic)

res_m = requests.get(
    'https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res_m.content

with open('D:\\Python\\test\\test_music.mp3', 'wb') as tm:
    tm.write(music)
