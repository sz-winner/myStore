# 将古诗词中的某一句抽出来，让学生填写


import _locale
_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])

with open('D:\\Python\\test.txt', 'r') as f:
    lines = f.readlines()  # 这时，lines 的数据存放在内存里。
# print(lines)  # 将读取到的内容打印出来，发现实际上读到的是带换行符的字符串。

with open('D:\\Python\\test.txt', 'w') as new:
    for line in lines:  # 在内存中，对数据进行处理，然后再写到文档里，覆盖之前的内容。
        if line not in ['0\n', '1\n']:  # 注意：这里的条件要根据上面打印出的数据写。
            new.write(line)

list_test = ['一弦一柱思华年。\n', '只是当时已惘然。\n']  # 将要默写的诗句放在列表里。
with open('D:\\Python\\poem2.txt', 'r') as f:
    lines = f.readlines()
# print(lines)
with open('D:\\Python\\poem2.txt', 'w') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)
