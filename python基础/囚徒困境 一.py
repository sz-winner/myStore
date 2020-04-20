# 场景一：假设有两名囚徒A和B因为合伙犯罪被抓捕，因没有确凿可以指认罪行的证据，审判者准备单独审判两位囚徒。
# 若两人都认罪，则两人各判10年；若一个认罪一个抵赖，则认罪的人判1年，抵赖的人判20年；若两人都抵赖，则各判3年。
while True:
    a = input('A，你认罪吗？')
    b = input('B，你认罪吗？')
    if a not in ['认罪', '不认罪'] or b not in ['认罪', '不认罪']:
        print('只能回答“认罪”或“不认罪”')
        continue
    elif a == b:
        if a == '认罪':
            print('各判10年')
        else:
            print('各判3年！')
        break
    else:
        if a == '认罪':
            print('A，判1年!\nB，判20年')
        else:
            print('A，判20年!\nB，判1年')
        break
    break
print('----game over----')
