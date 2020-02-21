# zip函数
def myzip(*iterables):
    iterator = [iter(it) for it in iterables]

    sentinel = None

    while True:
        lst = []

        for it in iterator:
            elem = next(it, sentinel)

            if elem is sentinel:
                return
            lst.append(elem)

        yield tuple(lst)
		
		
		

# 调用示例
n = myzip('123', 'ABCDE')

print(list(n))

# 实现的很好，简洁明了。后面自己要记得在代码里添加一些必要的注释，因为时间久了，很可能会忘记代码的逻辑结构。
