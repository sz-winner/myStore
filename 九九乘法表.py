#  九九乘法表
for n in range(1, 10):
    for i in range(1, n + 1):
        print('{} x {} = {}'.format(n, i, n * i), end="  ")
    print('\n')
