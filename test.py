# 考勤统计器
# 上班时间8:30，下班时间17:30，等于这个时间，不算迟到早退
# 迟到半小时内算迟到，超过半小时在1小时内，算旷工半天，迟到超过1小时，算旷工一天
# 每月允许3次忘记打卡
# 节假日及周末不上班
# 需要统计是否迟到、早退、旷工、加班、值班、调休
# import pandas.io.excel._openpyxl

import time

adv = '欢迎参加python小课学习班！'
# adv=input("请输入一段广告语：")
while 1:
    fx = input("请输入滚动的方向（L/R)").upper()  # 用upper()函数，表示将输入的字母强制转为大写
    if fx in ['L', 'R']:
        break
    print("您输入的有误，请重新输入！")

while 1:
    sd = input("请输入滚动的速度（请输入一个整数）:")
    if sd.isnumeric():
        break
    print("您输入的有误，请重新输入！")
while 1:
    if fx == "R":
        adv = adv[-1] + adv[:-1]
    else:
        adv = adv[1:] + adv[0]
    print('\r' + adv, end='', flush=True)
    time.sleep(int(sd))
