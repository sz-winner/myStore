# 深夜食堂开张记
import random   # 引入random模块
appetizer1 = ['话梅花生', '拍黄瓜', '凉拌三丝']
appetizer2 = ['豆腐脑', '冰镇绿豆糖水', '红枣银耳糖水']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer1)
        return a
    elif 5 < money < 10:
        a = random.choice(appetizer1)
        b = random.choice(appetizer2)
        return a, b


print(coupon(3))
print(coupon(6))
