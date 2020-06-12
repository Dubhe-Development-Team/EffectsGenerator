# by Cjsah, Gu_ZT
# 获取图片各个像素RGBA并生成particle指令
import os
from PIL import Image
from pathlib import Path

# 输入输出目录
# expi = Path()/'input'
expi = Path()/'input/1.png'
expo = Path()/'output/dust.mcfunction'

# 防重名
if os.path.exists(expo):
    os.remove(expo)

# 判断文件(夹)存在
if not os.path.exists(Path()/'input'):
    os.makedirs(Path()/'input')
if not os.path.exists(Path()/'output'):
    os.makedirs(Path()/'output')
with open(expo, "w") as f:
    pass

# 索引文件
imgname = os.listdir(Path())
delete = []
for i in imgname:
    if not i[-3:] == '.py':
        delete.append(i)
for i in delete:
    imgname.remove(i)

# 输入缩放文件大小
size = int(input('请输入你要转换成的图片大小(整数): '))

# 获取图片信息
im = Image.open(expi)
width = im.size[0]
height = im.size[1]
# 判断大小并缩放
if width > size or height > size:
    if width >= height:
        scale = size / width
    else:
        scale = size / height
    im = im.resize((round(width * scale), round(height * scale)), Image.ANTIALIAS)
    width = im.size[0]
    height = im.size[1]
# 获取像素点
pix = im.load()
im.show()

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
