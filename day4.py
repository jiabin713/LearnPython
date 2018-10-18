# 【战胜拖延症，组团学 Python】第二课
# 1. 掌握 Python 的 if-else 分支结构以及 while for 循环（包括 continue 和 break)
# 2. 编写一个程序，该程序可以从命令行接收一个数字输入并判断该数字是否为素数。

# 阅读链接中的 Python 基础部分，配合搜索可以完成此任务。



while True:
    num = int(input('输入一个自然数: '))
    for i in range(2, num):
        if num % i == 0:
            print(f'{num}不是素数')
            break
    else:
        print(f'{num}是素数')