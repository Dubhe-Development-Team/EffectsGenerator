# by Cjsah
# 获取图片各个像素RGBA并生成particle指令
import os
from PIL import Image

# 输入输出目录
expi = os.path.join(os.getcwd(), "1.png")
expo = os.path.join(os.getcwd(), "command.txt")
expr = os.path.join(os.getcwd(), "dust.mcfunction")

# 防重名
if os.path.exists(expo):
    os.remove(expo)
# 文件不存在时新建文件
with open(expo, "w") as f:
    pass

# 获取图片信息
im = Image.open(expi)
pix = im.load()
width = im.size[0]
height = im.size[1]

# 循环写入
for x in range(width):
    # 跳过透明像素
    for y in range(height):
        if pix[x, y][3] == 0:
            continue
        # 写入文件
        with open(expo, "r+") as f:
            f.read()
            f.write("particle dust ")
            f.write(str(pix[x, y][0] / 255))    # 计算 R 值
            f.write(" ")
            f.write(str(pix[x, y][1] / 255))    # 计算 G 值
            f.write(" ")
            f.write(str(pix[x, y][2] / 255))    # 计算 B 值
            f.write(" ")
            f.write(str(pix[x, y][3] / 255))    # 计算 A 值
            f.write(" ~")
            f.write(str('%.1f' % ((x - (width / 2)) / 10)))     # 计算 x 坐标
            f.write(" ~ ~")
            f.write(str('%.1f' % ((y - (height / 2)) / 10)))    # 计算 z 坐标
            f.write(" ~ ~ ~ 0 0 force\n")

# 改名(删除旧重名文件)
if os.path.exists(expr):
    os.remove(expr)
os.rename(expo, expr)
