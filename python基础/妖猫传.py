# 场景三：我很喜欢看电影，我回忆了一下，这两年我觉得还不错的国产电影。
# 下面，会将电影的影片名和主演放在字典里，如movie = {'妖猫传':['黄轩','染谷将太']}。
# 需要你补充一些代码，让其他人只要输入演员名，就打印出：××出演了电影××。
movies = {
    '妖猫传': ['黄轩', '染谷将太'],
    '无问西东': ['章子怡', '王力宏', '祖峰'],
    '超时空同居': ['雷佳音', '佟丽娅'],
}

actor = input('你想查询哪个演员？')
for movie in movies:  # 用 for 遍历字典，并将键值对定义为movie
    actors = movies[movie]  # 读取各部电影的主演人员
    if actor in actors:
        print(actor + '出演了电影' + movie)
print('----程序结束----')
