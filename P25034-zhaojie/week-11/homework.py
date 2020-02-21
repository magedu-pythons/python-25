#!/usr/bin/env python
# encoding:utf-8
# file: homework.py

# 自己实现python自带的map、zip和filter函数

# 还没学到 yield语法不熟 先简单实现


# 实现map函数
def my_map(*args):
    """文档字符串位置
    """
    if len(args) < 2:
        # 先不用异常的方式处理 只是打印
        print('map()至少需要两个参数')
    else:
        # 判断是否为可迭代对象 先不处理
        fnc_nme = args[0]
        new_tpl = args[1:]
        min_len = len(min(new_tpl, key=len))
        for idx in range(min_len):
            # yield后的代码会继续执行 yield只要存在函数就变成生成器
            yield fnc_nme(*[itr[idx] for itr in new_tpl])


# 实现zip函数
def my_zip(*args):
    if not len(args):
        return tuple()
    min_len = len(min(args, key=len))
    for idx in range(min_len):
        yield tuple(itr[idx] for itr in args)


# 实现filter函数
def my_filter(func, itr):
    if func is not None:
        for it in itr:
            if func(it):
                yield it
    else:
        for it in itr:
            if it:
                yield it


# 测试函数 加法
def func1(x, y):
    return x + y


# 测试函数 平方
def func2(x):
    return x ** 2


# 测试函数 取大于100的数
def func3(x):
    return True if x > 100 else False


if __name__ == '__main__':
    l1 = [3, 2, 3]
    l2 = [6, 5]
    print(list(my_map(func1, l1, l2)))
    print(list(my_zip([1, 2, 3], [4, 5], 'abcdefg')))
    print(list(my_filter(func3, [0, 201, 1, 2, 3, 100, 101])))
    print(list(my_zip()))
    print(list(my_filter(None, [0, 201, 1, 2, 3, 100, 101])))
    print('-------- 对照组 --------')
    print(list(map(func1, l1, l2)))
    print(list(zip([1, 2, 3], [4, 5], 'abcdefg')))
    print(list(filter(func3, [0, 201, 1, 2, 3, 100, 101])))
    print(list(zip()))
    print(list(filter(None, [0, 201, 1, 2, 3, 100, 101])))

# 代码实现的很好，在测试的时候可以多考虑几种异常情况，或者说刻意给一些不正常的测试用例
# 来测试代码的健壮性。
