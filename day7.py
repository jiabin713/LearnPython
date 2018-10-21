# # 战胜拖延症，组团学 Python】第五课：
# # 1. 回顾前面所学的内容
# # 2.在无参考资料的前提下，尽量多的写下你能回忆起的 Python 知识。

# # 特殊的打卡方式：将你回忆的知识发布在沸点，评论留下你的沸点链接。


# # 输入输出
# input('提示符')
# 输入的都是字符串
# a, b, c = 'a', 'b', 'c'
# print(f'abc{a}, {b}, {c}', end=' ')
# print('{}, {}, {}'.format(a, b , c))

# # 数据类型
# # str
# s = 'abcd'
# s.split('')  # ['a', 'b', 'c', 'd']
# s.lower() # 'abcd'
# s.upper() # 'ABCD'
# s.title() # 'Abcd'
# s.capitalize() #'Abcd'
# int
# float
# dict
# list #序列从0开始
# set
# tuple
# bool

# 运算符
# + # 字符串相加，拼接字符串
# -
# * # 字符串 * 整数 'a' * 3 => 'aaa'
# /
# % # 余数
# divmod(7, 2) #(3, 1) 结果为除数和余数

# 函数
# def function_name():
#     pass

# 没有return 或只有return 返回None
# 可以返回函数

# def fun(*args, **kwargs):
#     pass

# *args 接收一串参数, 如果是列表,可以把列表解压传入, *list
# **kwargs 接收一串键值对, 如果是字典,可以把列表解压传入, **dict


# 循环

# for i in range(100):
#     pass

# range(0:100:2)
# 默认从零开始,不包括第二个参数,第三个是步进

# while condition:
#     pass

# 循环中有
# break 跳出循环
# continue 跳过


# 判断
# if bool:
#     pass
# elif bool:
#     pass
# else:
#     pass

# 生成器
# 列表生成式
# [x * x for x in range(10) if x % 2 == 0]
# 生成器函数中有yield
# 每次next 执行到 yield

# 迭代器
# 可迭代不一定是迭代器
# Iterable 和 Iterator
# 使用内置函数iter() 变成迭代器
# 可以for循环的是可迭代的
# 有内置函数__next__是迭代器