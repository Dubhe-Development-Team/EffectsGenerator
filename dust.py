# by Cjsah
# 彩色光环
import math
import os
import seaborn as sns
import matplotlib.pyplot as plt

# 初始化
z = 0
c = 0
v = 0
rgbvalue = []
exp1 = os.path.join(os.getcwd(), "command.txt")
exp2 = os.path.join(os.getcwd(), "dust.mcfunction")

# 半径
cr = 2.5

# 粒子数，需可被360整除
times = 60
x = 360 // times


# RGB格式颜色转为16进制颜色格式
def rgb_to_hex(rgb):
    rgb = rgb.split(',')  # 将RGB格式划分开
    color = '#'
    for i in rgb:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').upper()
    # print(color)
    return color


# RGB格式颜色转为16进制颜色格式
def rgb_list_to_hex(rgb):
    # RGB = rgb.split(',')  # 将RGB格式划分开
    color = '#'
    for i in rgb:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        color += str(hex(num))[-2:].replace('x', '0').upper()
    # print(color)
    return color


# 16进制颜色格式颜色转为RGB格式
def hex_to_rgb(hex1):
    r = int(hex1[1:3], 16)
    g = int(hex1[3:5], 16)
    b = int(hex1[5:7], 16)
    rgb = str(r) + ',' + str(g) + ',' + str(b)
    # print(rgb)
    return rgb, [r, g, b]


# 生成渐变色
def gradient_color(color_list, color_sum=360):
    color_center_count = len(color_list)
    # if color_center_count == 2:
    #     color_center_count = 1
    color_sub_count = int(color_sum / (color_center_count - 1))
    color_index_start = 0
    color_map = []
    for color_index_end in range(1, color_center_count):
        color_rgb_start = hex_to_rgb(color_list[color_index_start])[1]
        color_rgb_end = hex_to_rgb(color_list[color_index_end])[1]
        r_step = (color_rgb_end[0] - color_rgb_start[0]) / color_sub_count
        g_step = (color_rgb_end[1] - color_rgb_start[1]) / color_sub_count
        b_step = (color_rgb_end[2] - color_rgb_start[2]) / color_sub_count
        # 生成中间渐变色
        now_color = color_rgb_start
        color_map.append(rgb_list_to_hex(now_color))
        for color_index in range(1, color_sub_count):
            now_color = [now_color[0] + r_step, now_color[1] + g_step, now_color[2] + b_step]
            color_map.append(rgb_list_to_hex(now_color))
        color_index_start = color_index_end
    return color_map


# 渐变
if __name__ == '__main__':
    # 在此填入渐变颜色
    input_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#00FFFF",
                    "#00B9FF", "#0000FF", "#6F00FF", "#A200CC", "#FF0000"]
    colors = gradient_color(input_colors)
    sns.palplot(colors)
    while v < len(colors):
        rgbvalue.append(colors[v])
        v += len(colors) // times
    # print(len(colors))
    # print(len(rgb))
    # print(rgb)
    # plt.show()

# 防重名文件
if os.path.exists(exp1):
    os.remove(exp1)

# 写入文件:重置
with open(exp1, "w") as f:
    f.write("scoreboard players reset @s fly_jtpk_bst\n")

# 写入文件:粒子
while z < 360:

    c = z // x

    with open(exp1, "r+") as f:
        f.read()
        f.write("particle dust ")
        f.write(str(((int(rgbvalue[c][1], 16)) * 16 + (int(rgbvalue[c][2], 16))) / 255))
        f.write(" ")
        f.write(str(((int(rgbvalue[c][3], 16)) * 16 + (int(rgbvalue[c][4], 16))) / 255))
        f.write(" ")
        f.write(str(((int(rgbvalue[c][5], 16)) * 16 + (int(rgbvalue[c][6], 16))) / 255))
        f.write(" 1 ^")
        f.write(str('%.2f' % (math.cos(math.radians(z)) * cr)))
        f.write(" ^")
        f.write(str('%.2f' % (math.sin(math.radians(z)) * cr)))
        f.write(" ^-1 ~ ~ ~ 0 0 normal\n")

    z += x

# 删旧文件加新文件
if os.path.exists(exp2):
    os.remove(exp2)
os.rename(exp1, exp2)
