# 自己实现python自带的map、zip和filter函数
# g = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# print(list(g))
#map函数
def map1(fn,*iterable):
    argnum = len(iterable)
    if argnum == 0:
        raise TypeError('map1() must have at least two arguments.')
    #找到所有序列中的最短长度
    minlen = len(iterable[0])
    for it in iterable:
        if len(it) < minlen:
            minlen = len(it)

    #获得函数的参数列表
    lst = []
    for i in range(minlen):
        tmp = [0] * argnum
        for j in range(argnum):
            tmp[j] = iterable[j][i]
        lst.append(tmp)
    # 执行函数，返回生成器
    for arg in lst:
        yield fn(*arg)

g = map1(lambda x, y: x + y,[1,2,3],[5,6,7])
print(next(g))

#zip函数
def zip1(*iterable):
    argnum = len(iterable)
    #找到所有序列中的最短长度
    minlen = len(iterable[0])
    for it in iterable:
        if len(it) < minlen:
            minlen = len(it)

    #获得列表
    # lst = []
    for i in range(minlen):
        t = ()
        for j in range(argnum):
            t += (iterable[j][i],)
        yield t

print(zip1([1,2,3],['a','b']))

#filter函数
def filter1(fn,iterable):
    for it in iterable:
        if fn(it):
            yield it

f1 = filter1(lambda x:x%2,[1,2,3,4,5,6,7,8])
print(next(f1))




