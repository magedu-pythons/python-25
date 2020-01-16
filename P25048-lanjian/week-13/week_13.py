# 实现一个timeit的装饰器：timeit 装饰能够计算被装饰函数的运行时间
import datetime
import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        装饰器函数
        :param args:
        :param kwargs:
        :return:
        """
        starttime = datetime.datetime.now()
        print('wrapper function begin')
        result = func(*args, **kwargs)
        duration = (datetime.datetime.now() - starttime).total_seconds()
        print('wrapper function finish,result= {},cost {}s'.format(result, duration))
        return result

    return wrapper


@timeit
def test(x: int, y: int, *args: int, z: int, w: int = 30, **kwargs: int) -> int:
    """
    被装饰函数
    :param x:
    :param y:
    :param args:
    :param z:
    :param w:
    :param kwargs:
    :return:
    """
    print('wrapped function begin')
    result = x + y
    for i in args:
        result += i

    result += z
    result += w
    for _, v in kwargs.items():
        result += v

    time.sleep(3)

    print('wrapped function calculate finish,sum=', result)
    return result


# print(test.__doc__)
print(test(1, 2, 3, 4, 5, 6, z=7, a=8, b=9, c=10))
