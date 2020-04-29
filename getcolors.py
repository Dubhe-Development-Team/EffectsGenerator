# by Cjsah
# 获取图片各个像素RGBA并生成particle指令
import os
from PIL import Image

expi = os.path.join(os.getcwd(), "1.png")
expo = os.path.join(os.getcwd(), "command.txt")

if os.path.exists(expo):
    os.remove(expo)

with open(expo, "w") as f:
    pass

im = Image.open(expi)
pix = im.load()
width = im.size[0]
height = im.size[1]

for x in range(width):
    for y in range(height):
        if pix[x, y][3] == 0:
            continue

        with open(expo, "r+") as f:
            f.read()
            f.write("particle dust ")
            f.write(str(pix[x, y][0] / 255))
            f.write(" ")
            f.write(str(pix[x, y][1] / 255))
            f.write(" ")
            f.write(str(pix[x, y][2] / 255))
            f.write(" ")
            f.write(str(pix[x, y][3] / 255))
            f.write(" ~")
            f.write(str('%.1f' % ((x - (width / 2)) / 10)))
            f.write(" ~ ~")
            f.write(str('%.1f' % ((y - (height / 2)) / 10)))
            f.write(" ~ ~ ~ 0 0 force\n")
