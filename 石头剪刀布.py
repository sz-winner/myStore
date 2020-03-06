# 石头剪刀布：和电脑玩一个剪刀石头布的游戏：电脑随机出拳，我们可选择出什么。


import random

punches = ['石头', '剪刀', '布']
computer_choice = random.choice(punches)
user_choice = input('请出招：【石头，剪刀，布】 ')
while user_choice not in punches:
    print('兄弟，你出招的姿势不对！')
    user_choice = input('请重新出招：【石头，剪刀，布】 ')
if computer_choice == user_choice:
    print('电脑出的也是%s，双方打平' % (computer_choice))
# elif (computer_choice == '石头' and user_choice == '剪刀') or (computer_choice == '剪刀' and user_choice == '布') or (computer_choice == '布' and user_choice == '石头'):
elif user_choice == punches(punches[computer_choice.index] - 1):
    # 注意上面这个语句的写法: 电脑的选择有3种，索引位置分别是：0石头、1剪刀、2布, 假设在电脑索引位置上减1，对应：-1布，0石头，1剪刀，皆胜
    print('电脑出的是%s，你输了！' % computer_choice)
else:
    print('电脑出的是%s，你赢了！' % computer_choice)
