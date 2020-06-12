# by Cjsah, Gu_ZT
# 获取图片各个像素RGBA并生成particle指令
import os
from PIL import Image
import math


# 输入输出目录
expi = os.path.join(os.getcwd(), "1.png")
expo = os.path.join(os.getcwd(), "dust.mcfunction")

# 防重名
if os.path.exists(expo):
    os.remove(expo)

# 文件不存在时新建文件
with open(expo, "w") as f:
    pass

# 获取图片信息
im = Image.open(expi)
if im.size[0] > 128 and im.size[1] > 128:
    # 目前只有方形图片可用
    im = im.resize((128, 128))
pix = im.load()
width = im.size[0]
height = im.size[1]

# 循环写入
for x in range(width):
    for z in range(height):
        # 跳过透明像素
        if pix[x, z][3] == 0:
            continue
        # 写入文件
        with open(expo, "r+") as f:
            f.read()
            f.write("particle dust ")
            f.write(str(pix[x, z][0] / 255))    # 计算 R 值
            f.write(" ")
            f.write(str(pix[x, z][1] / 255))    # 计算 G 值
            f.write(" ")
            f.write(str(pix[x, z][2] / 255))    # 计算 B 值
            f.write(" ")
            f.write(str(pix[x, z][3] / 255))    # 计算 A 值
            f.write(" ~")
            f.write(str('%.1f' % ((x - (width / 2)) / 10)))     # 计算 x 坐标
            f.write(" ~ ~")
            f.write(str('%.1f' % ((z - (height / 2)) / 10)))    # 计算 z 坐标
            f.write(" ~ ~ ~ 0 0 force\n")
