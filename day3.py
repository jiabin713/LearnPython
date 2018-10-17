# 【战胜拖延症，组团学 Python】第一课：
# 1. 掌握 Python 变量，输入输出，+-*/%运算
# 2. 编写 Python 程序，此程序可以从命令行接收一个数字输入，并输出以该数字为半径的圆的周长和面积。

# 阅读 Learn Python3 the hardway  Exercise1 至 Exercise8 + Google 搜索可以完成此次打卡任务。


import math

r = float(input('输入一个半径'))
PI = math.pi
perimeter = 2 * PI * r
area = PI * pow(r, 2)

print(f'该数字{r}为半径的圆的周长为{perimeter:.2f}')
print(f'该数字{r}为半径的圆的面积为{area:.2f}')