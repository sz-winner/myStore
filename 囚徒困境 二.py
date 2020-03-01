#场景二：上一个练习，我们将“囚徒困境”写成了代码，让程序收集两名囚犯的认罪情况，进而决定他们的判决：
#两人都认罪，则各判10年；一个认罪一个抵赖，则前者判1年，后者判20年；两人都抵赖，各判3年。只有两人都不认罪，程序才会停止。
#现在有一个社会学家，在不同的人群中做这个实验，一旦遇到都不认罪的情况，就停止该人群中的实验。
#同时，他希望程序能记录每一对实验者的选择，以及记录第几对实验者都选择不认罪。请你帮帮他吧。

i=0
list1=[]	
while True:
    i=i+1
    a=input('A'+str(i)+'，你认罪吗？')
    b=input('B'+str(i)+'，你认罪吗？')
    # 需要将每一对实验者的选择存起来。
    list1.append([a,b])
    if a not in ['认罪','不认罪'] or b not in ['认罪','不认罪']:
        print('只能回答“认罪”或“不认罪”')
        continue
    elif a==b:
        if a=='认罪':
            print('各判10年')
            continue
        else:
            print('各判3年！')
            print('两个人都不认罪，实验终止！')
            print('第'+str(i)+'对实验者做出了最优选择')
        break
    else:
        if a=='认罪':
            print('A，判1年!\nB，判20年')
        else:
            print('A，判20年!\nB，判1年')
        continue
    break
# 通过循环打印每一对实验者的选择。
print('-----------------')
for n in range(i):
    print('[A'+str(n+1)+',B'+str(n+1)+']的选择是：'+str(list1[n]))
print('----game over----')

#字典中键和键值的运算举例
scores = {'小明': 95, '小红': 90, '小刚': 90}
for i in scores:
    print(i,scores[i])
