import random

all = ['正面', '反面']
guess = ''

while guess not in all:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')

toss = all[random.randint(0, 1)]
# 随机抛硬币，all[0]取出正面，all[1]取出反面

if toss == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，再给你一次机会。')
    guess = input('再输一次“正面”或“反面”：')
    if toss == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')
