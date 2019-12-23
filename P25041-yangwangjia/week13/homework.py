import datetime
import time


def timeit(runtime=False):
    """ 本装饰器实现了时间统计功能。

    通过datetime模块实现函数运行时间检查，装饰器可以选择是否传参。
    默认为不传参，当不传参时，装饰器不会进行耗时检查。
    当传参后首先进行传参类型检查，如果是float\int类型继续进行后续操作，否则抛出异常TypeError。
    然后程序运行耗时和runtime进行大小比较，满足运行耗时要求输出通过耗时的程序验证！，并输出程序运行时间。
    如果耗时超过所传参数，抛出异常TimeoutError，在异常中序显示执行时间，和`这个程序太垃圾了，抓紧优化！`
    :param runtime: 接收int\float类型参数，该参数为函数耗时校验的参数单位是S
    :return:返回字符串类型
    """
    def _timeit(fn):
        def wrapper(*args,**kwargs):
            start_time = datetime.datetime.now()
            # 调用者函数
            ret = fn(*args,**kwargs)

            end_time = datetime.datetime.now()
            Delta = (end_time - start_time).total_seconds()  # 获取函数运行耗时

            if runtime:
                if not isinstance(runtime, (int, float)):  # 判断装饰器传参是否正确，如果不是float\int类型直接抛异常。
                    raise TypeError("Wrapper receives int type parameter! got {}".format(type(runtime)))
                if Delta > runtime:
                    # print("run time `{}`，The program is too spicy. Hurry to optimize it!".format(Delta))
                    raise TimeoutError("run time `{}` S，The program is too spicy. Hurry to optimize it!".format(Delta))
                else:
                    print("run time `{}` S，Pass the time-consuming verification of the program!".format(Delta))

            else:
                print("run time `{}`".format(Delta))
            return ret
        return wrapper
    return _timeit


@timeit(1)  # 可以传参，也可以不传参，传参表示开启程序耗时校验
def add(x: int, y: int)->int:
    """ 这是一个测试函数，由此函数来测试timeit装饰器函数

    :param x:int类型的整数
    :param y:int类型的整数
    :return:x+y的值
    """
    time.sleep(0.6)
    return x+y


if __name__ == "__main__":
    # add 是提供的一个测试装饰器的函数
    print(add(3, 4))
