# 【战胜拖延症，组团学 Python】第三课：
# 1. 了解 Python 的基本数据结构和函数
# 2. 将第二课中的程序改写成函数的形式。任意编写一个 List 作为函数的参数，判断 List 中的每个元素是否为素数。并将是素数的元素打印为字典。（可以随意设置 key）

# 阅读链接中的函数部分配合搜索可以完成此任务。


def is_prime(num):
    if isinstance(num, int) and num > 0:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
           return True
    else:
        return False

def prime(num_list):
    prime_dict = {}
    for num in num_list:
        if is_prime(num):
            prime_dict[num] = 'yes'
    return prime_dict

list = ['1',2,3,4.4,'123',5,6,7,8,9,10]

print(prime(list))