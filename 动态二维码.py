from MyQR import myqr
import os

version, level, qr_name = myqr.run(
    words="https://shop473196137.taobao.com/?spm=a230r.7195193.1997079397.2.1b944a4eHcm1Ln",  # 可以是字符串，也可以是网址(前面要加http(s)://)
    version=1,  # 设置容错率为最高
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture="D:\\Python\\qr_photo.gif",  # 将二维码和图片合成
    colorized=True,  # 黑白还是彩色，True是彩色二维码
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    brightness=1.0,  # 用来调节图片的亮度，其余用法和取值同上
    save_name="D:\\Python\\myqr_test.gif",  # 保存文件的名字，格式可以是jpg,png,bmp,gif
    save_dir=os.getcwd()  # 控制位置
)
