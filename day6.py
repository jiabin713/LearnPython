# 【战胜拖延症，组团学 Python】第四课：
# 1. 掌握链接中 Python 教程的高级特性
# 2. 利用生成器生成斐波那契数列


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

if __name__ == '__main__':
    max = int(input('需要几个斐波那契数'))
    # fib_list = []
    # for i in fib(max):
    #     fib_list.append(i)
    # print(fib_list)
    print(list(fib(max)))
