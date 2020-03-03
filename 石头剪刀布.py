# 石头剪刀布：和电脑玩一个剪刀石头布的游戏：电脑随机出拳，我们可选择出什么。


import random

punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = input('请选择你的攻击方案：1-石头，2-剪刀，3-布',punches)
if user_choice not in punches:
    print('请在1-3中选择一个数字输入')
elif:
    computer_choice == computer_choice
    print('双方打平')
elif:
    