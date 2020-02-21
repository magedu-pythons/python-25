# filter函数

def myfilter(func, iterable):
    lst = []

    for c in iterable:
        if func(c):
            yield c



# 调用示例
g = myfilter(lambda x: x > 3, (1, 2, 3, 5, 6))
print(list(g))

# 可以实现正常情况下的基本功能，没有考虑代码异常的情况。
