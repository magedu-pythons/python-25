# 自己实现python自带的map、zip和filter函数
# g = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# print(list(g))
#map函数
from inspect import isfunction
from collections import Iterable
def map1(fn,*iterable):
    '''
    fn函数应用于iterable的每一个元素，结果以生成器的形式返回
    :param fn: 函数
    :param iterable: 可迭代对象，例如列表，字符串，元组等
    :return:生成器对象
    '''
    #判断第一个参数是否为函数，若不是，抛异常
    if isfunction(fn) is False:
        raise TypeError("'fn'object is not callable")
    #判断iterable中的元素是否为可迭代对象，若不是可迭代对象，抛异常
    for it in iterable:
        _typename = type(it).__name__
        if not isinstance(it,Iterable):
            raise TypeError("'"+_typename +"'"+" object is not iterable")

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

#zip函数
def zip1(*iterable):
    '''
    从参数中的多个迭代器取元素组合成一个新的迭代器
    :param iterable: 可迭代对象
    :return: 生成器对象
    '''
    #判断iterable中的元素是否为可迭代对象，若不是可迭代对象，抛异常
    for it in iterable:
        _typename = type(it).__name__
        if not isinstance(it,Iterable):
            raise TypeError("'"+_typename +"'"+" object is not iterable")

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

#filter函数
def filter1(fn,iterable):
    '''
    对序列数据进行过滤，函数判断为真的保留，获得一个生成器对象
    :param fn: 函数，返回值为布尔类型
    :param iterable: 可迭代对象
    :return: 生成器对象
    '''
    #判断第一个参数是否为函数，若不是，抛异常
    if isfunction(fn) is False:
        raise TypeError("'fn'object is not callable")
    #判断iterable中的元素是否为可迭代对象，若不是可迭代对象，抛异常
    _typename = type(iterable).__name__
    if not isinstance(iterable,Iterable):
        raise TypeError("'"+_typename +"'"+" object is not iterable")

    for it in iterable:
        if fn(it):
            yield it



if __name__ == '__main__':
    # 测试map1:正常情况
    g = map1(lambda x, y: x + y, [1, 2, 3], [5, 6, 7])
    print(next(g))

    #测试map1：第一个参数不是函数
    try:
        g = map1(4, [1, 2, 3], [5, 6, 7])
        print(next(g))
    except Exception as e:
        print('map异常测试1:',e)

    # 测试map1：第一个参数之后的参数不为可迭代对象
    try:
        g = map1(lambda x:x+1, 7)
        print(next(g))
    except Exception as e:
        print('map异常测试2:',e)
    print('------------------------------------')
    # 测试zip1：正常测试
    print(next(zip1([1, 2, 3], ['a', 'b'])))
    # 测试zip1：参数不为可迭代对象测试
    try:
        print(next(zip1(5, ['a', 'b'])))
    except Exception as e:
        print('zip异常测试:',e)

    print('------------------------------')
    # 测试filter1:正常测试
    f1 = filter1(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8])
    print(next(f1))
    # 测试filter1:第一个参数不为函数
    try:
        f1 = filter1(4, [1, 2, 3, 4, 5, 6, 7, 8])
        print(next(f1))
    except Exception as e:
        print('filter异常测试1:',e)

    # 测试filter1:第二个参数为不可迭代对象
    try:
        f1 = filter1(lambda x: x % 2, 6)
        print(next(f1))
    except Exception as e:
        print('filter异常测试2:', e)



# 功能实现的非常好，基本的异常也都考虑到了，也知道写测试代码来测试，比第11周的要好。
