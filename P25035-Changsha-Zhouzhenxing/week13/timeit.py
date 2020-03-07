# 第十三周作业
# 本周作业：实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间

import datetime
import time
import functools


# timeit装饰器
def timeit(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        starttime = datetime.datetime.now()

        ret = fn(*args, **kwargs)

        endtime = datetime.datetime.now()

        print('计算运行时间：{}秒'.format((endtime- starttime).total_seconds()) )

        return ret

    return wrapper



@timeit
def add(x:int, y:int) -> int:
    time.sleep(1)
    return x + y


add(3, 3)
