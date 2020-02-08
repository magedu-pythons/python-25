# filter函数

def myfilter(func, iterable):
    lst = []

    for c in iterable:
        if func(c):
            yield c



# 调用示例
g = myfilter(lambda x: x > 3, (1, 2, 3, 5, 6))
print(list(g))