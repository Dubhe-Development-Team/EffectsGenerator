# by Cjsah
import os

# 初始化
i = 0
expi = os.path.join(os.getcwd(), "1.yml")
expo = os.path.join(os.getcwd(), "command.txt")

# 防重名文件
if os.path.exists(expo):
    os.remove(expo)

# 写入文件:重置
with open(expi) as file:
    for text in file:
        with open(expo, "") as f:
            file.read()
            file.write(str(((int(text[i][1], 16)) * 16 + (int(text[i][2], 16))) / 255))
            file.write(" ")
            file.write(str(((int(text[i][3], 16)) * 16 + (int(text[i][4], 16))) / 255))
            file.write(" ")
            file.write(str(((int(text[i][5], 16)) * 16 + (int(text[i][6], 16))) / 255))
            file.write("\n")

