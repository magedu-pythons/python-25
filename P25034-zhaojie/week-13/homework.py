#!/usr/bin/env python
# encoding:utf-8
# file: homework

# 实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间

import time
from functools import wraps


def my_timeit(timer=lambda: time.time(), number=1000000):
    def _timeit(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            sum_t = 0
            ret = None
            for i in range(number):
                start_t = timer()
                ret = fn(*args, **kwargs)
                sum_t += timer() - start_t
            print(sum_t)
            return ret
        return wrapper
    return _timeit


# @my_timeit 为错误装饰方式，等价式如下：
# @my_timeit => func=my_timeit(func) => func=my_timeit(timer=func,number=1000000) =>
# func=_timeit => func([4]) 相当于调用 _timeit([4]) => wrapper，最后返回wrapper而不是执行wrapper


# 如下等价式：func=my_timeit()(func) => func=my_timeit(默认参数)(func) =>
# func=_timeit(func) => func=wrapper => func([4]) 相当于调用 wrapper([4])
@my_timeit()
def func(lst):
    return [1, 2, 3] + lst


@my_timeit(number=10)
def func2(lst):
    return [1, 2, 3] + lst


# 使用纳秒计数器time.perf_counter
@my_timeit(timer=time.perf_counter, number=10)
def func3(lst):
    return [1, 2, 3] + lst


print(func([4]))
print('~~~~~~~~~~~~~~~')
print(func2([4]))
print('~~~~~~~~~~~~~~~')
print(func3([4]))
