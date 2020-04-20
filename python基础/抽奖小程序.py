import random
import time


def luckystar(*name):  # 设计不定长参数
    luckylist = []  # 定义列表
    for i in name:  # 轮询传入的参数个数
        luckylist.append(i)  # 将参数值逐个填入列表
    luckylist1 = random.choice(luckylist)
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜' + luckylist1 + '中奖！')


luckystar('张三', '李四', '王五', '孙六', '小刚', '小红', '小明', '小花')
