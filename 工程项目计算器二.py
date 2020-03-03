# 工时计算器
# 已知项目大小、工作人数，计算需要多少工时才能完成
# 或者已知项目大小、总工时，计算要在这样的共识内完成工作，至少需要的工作人数
# 标准大小的项目，需要1个人80个工时完成（也就是10个人天）
# 某项目所需总工时 =（项目大小 / 标准项目） * 工人数量
# 某项目完工所需人数 = （项目大小 / 标准项目） / 完工时间


import math


def estimate_workers(size, time):
    # 人力计算：如果参数中填了时间，没填人数，就计算人力
    # if (number == None) and (time != None):
    size = float(input('请输入项目大小：\n'))
    time = int(input('请输入工期数:\n'))
    number = math.ceil(size * 80 / time)
    print('项目大小为%.1f个标准项目，如果需要在%.1f天的工期内完成，则需要人力数量为：%d人' % (size, time, number))
    # 工时计算：如果参数中填了人数，没填时间，就计算工时
    # elif (number != None) and (time == None):


def estimate_period(size, number):
    size = float(input('请输入项目大小：\n'))
    number = int(input('请输入人力数量:\n'))
    time = size * 80 / number
    print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工期为：%.1f天' % (size, number, time))


def main():
    while again:
        print('----欢迎使用工程项目计算器----')
        types = int(input('请选择计算类型：1-人力计算，2-工期计算\n'))
        if types == 1:
            estimate_period(0, 0)
        elif types == 2:
            estimate_workers(0, 0)
        else:
            print('输入错误，只能输入‘1’或‘2’：')
        q1 = print('是否要继续计算？继续请输入y或Y，否则退出')
        if q1 not in('y', 'Y'):
            again = False
        print('----程序结束----')


main()
