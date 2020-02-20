#实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间
from functools import wraps
import datetime

def timeit(fn):
    @wraps(fn) #使用内建wraps函数保证使用装饰器后函数属性不改变
    def inner(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        travel = (datetime.datetime.now()-start).total_seconds()
        msg = 'fn:{},take time:{} seconds'.format(fn.__name__,travel)
        print(msg)
        return ret
    return inner

@timeit   #等价式 testfunc = timeit(testfunc) =wrap(testfunc) = fn
def testfunc(times=1000000):
    #测试函数
    count = 0
    for i in range(times):
        count += 1
    return count

print(testfunc(100000000))

# 实现的很好，说明这部分的内容看到了，代码没有问题。后面装饰器在生产上应用的非常多，希望可以好好吸收这部分的内容                   
