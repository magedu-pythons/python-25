###实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间

import datetime

def copy_properties(src,dst):
    dst.__name__ = src.__name__
    dst.__doc__ = src.__doc__

def try_timeit(fn,number=10000):
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        for _ in range(number):
            fn(*args,**kwargs)
        t = (datetime.datetime.now() - start).total_seconds()
        print('{} seconds for {} runs'.format(t,number))
        c = fn(*args,**kwargs)
        return c
    copy_properties(fn,wrapper)
    return wrapper

@try_timeit
def add(x,y):
    return x**2 + y**2

a = add(4,5)
print(a)

# 实现的很好，但是不要在内部放1000次循环，因为你不知道别人会怎么调用你写的装饰器，如果别人此时
# 在装饰器外部也使用1000次循环或者使用的函数比较耗时，此时就比较麻烦。
