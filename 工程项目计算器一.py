# 工时计算器
# 已知项目大小、工作人数，计算需要多少工时才能完成
# 或者已知项目大小、总工时，计算要在这样的共识内完成工作，至少需要的工作人数
# 标准大小的项目，需要1个人80个工时完成（也就是10个人天）
# 某项目所需总工时 =（项目大小 / 标准项目） * 工人数量
# 某项目完工所需人数 = （项目大小 / 标准项目） / 完工时间


import math


# 为函数设置了三个参数，并都带有默认参数
def estimated(types, size, other):
    # 人力计算：如果参数中填了时间，没填人数，就计算人力
    # if (number == None) and (time != None):
    size = float(input('请输入项目大小：\n'))
    types = input('请选择计算类型：1-人力计算，2-工时计算\n')
    if types == '1':
        other = int(input('请输入工时数量:\n'))
        number = math.ceil(size * 80 / other)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, other, number))
    # 工时计算：如果参数中填了人数，没填时间，就计算工时
    # elif (number != None) and (time == None):
    elif types == '2':
        other = int(input('请输入人力数量:\n'))
        time = size * 80 / other
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, other, time))


estimated(0, 0, 0)
