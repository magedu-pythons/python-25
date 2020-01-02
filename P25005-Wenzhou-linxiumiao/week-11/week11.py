#模拟map函数
def try_map(f,*args):
    """
    模拟map内置函数的功能
    :param f:
    :param args:
    :return:
    """
    #设置一个开关 来判断进函数f的参数个数
    flag = False
    if len(args) >= 2:
        flag = True
    #假如进入函数的参数有两个
    if flag:
        fir_ite = args[0]
        oth_ite = args[1]
        l = min(len(fir_ite),len(oth_ite))
        for x in range(l):
            yield f(fir_ite[x],oth_ite[x])
    #假如进入函数的参数只有一个
    else:
        for x in args[0]:
            yield f(x)

list1 = [-2,1,2,3]
list2 = [2,3]

#两参函数
def f(x,y):
    return x+y

#单参函数
def add1(x):
    return x+2

for i in try_map(f,list1,list2):
    print(i)

for i in try_map(add1,list1):
    print(i)

#模拟zip函数
def try_zip(*args):
    """
    ZIP函数实现
    :param args:
    :return:
    """
    s = object()
    ite = [iter(i) for i in args]
    while ite:
        r = []
        for i in ite:
            e = next(i,s)
            if e is s:
                return
            r.append(e)
            yield tuple(r)

for i in zip('abc','12'):
    print(i)

def try_filter(f,args):
    """
    实现filter函数
    :param f:
    :param args:
    :return:
    """
    r = []
    for i in args:
        if f(i):
            r.append(i)
    yield r

print(try_filter(add1,list1))
for i in try_filter(add1,list1):
    print(i)