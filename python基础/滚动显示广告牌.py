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
    if sd.isnumeric():  # 判断输入的是否有效的数字
        break
    print("您输入的有误，请重新输入！")
while 1:
    if fx == "R":
        adv = adv[-1] + adv[:-1]
    else:
        adv = adv[1:] + adv[0]
    print('\r' + adv, end='', flush=True)
    time.sleep(int(sd))
