from inspect import isfunction


def my_fun(*args, **kwargs):
    """ 自己实现python自带的map、zip和filter函数

    :param args: 位置参数，第一个为调用函数名称，接收一个str类型，
                在调用map函数时:第二个是待转换类型。该参数同时接受函数类型参数。

                在调用zip函数时:从第二个参数开始为可迭代对象。
                在最短的迭代对象迭代完成后停止，此时若继续调用next抛出StopIteration，函数返回值为一个生成器对象。

                在调用zip函数时:第二个为函数参数，此参数为缺省参数默认为None
                第三各参数为iterable可迭代对象，若函数指定为None，则过滤掉iterable中为false的值，
                否则过滤掉函数返回false的值，之后返回一个生成器对象，如果调用超过可迭代对象的长度，
                此时若继续调用next抛出StopIteration，函数返回值为一个生成器对象。

    :param kwargs:传递一个可迭代对象名字为iters,仅在调用map函数时使用
    :return:
    """

    def _map(_type, _iter: iter):
        """  自定义实现map函数

        :param _type: 转换类型
        :param _iter:可迭代对象
        :return:生成器对象
        """
        _args = {int, str, tuple, set}
        # 调用者为函数,或者为上述声明类型中的一种类型转换
        if _type in _args or isfunction(_type):
            _ret = (_type(i) for i in _iter)
        else:
            raise TypeError("got type error:",_type)

        return _ret

    def _zip(iters: tuple):
        """ 自定义实现zip函数

        :param iters: 参数为元祖元祖中是可迭代对象
        :return:
        """
        # 获取传入的iterable中长度最短的，以此为标准组成新元组返回。
        length = sorted((len(i) for i in iters))[0]
        for i in range(length):
            tmp = [j.pop() if type(j) is set else j[i] for j in iters]
            yield tuple(tmp)

    def _filter(fun, iters: iter):

        """ 自定义实现filter函数

        :param fun: 传入函数参数，函数参数可以传递None
        :param iters: 传入可迭代对象，函数若传入None则过滤掉iterable中的假值
        :return:
        """

        for i in iters:
            if i:
                if fun:
                    if fun(i):
                        _ret = i
                    else:
                        continue
                else:
                    _ret = i

                yield _ret

    # 函数调用
    def params(*args, **kwargs):
        dic = kwargs
        fun = args[0]
        ret = None
        if fun == 'map':
            _type = args[1]
            _iters = dic.get('iters')
            ret = _map(_type, _iters)
        elif fun == 'zip':
            ret = _zip(args[1:])
        else:
            ret = _filter(args[1],args[2])
        return ret

    return params(*args, **kwargs)


if __name__ == "__main__":
    # 帮组文档
    print(my_fun.__doc__)

    # 测试用例
    # map
    my_fun__map = my_fun('map', int, iters=[1,3,4])
    print(my_fun__map)
    for i in my_fun__map:
        print(i)
    my_fun__map = my_fun('map', lambda x:x**2, iters=[1,3,4])
    print(my_fun__map)
    for i in my_fun__map:
        print(i)

    # zip
    my_fun_zip = my_fun('zip',[1,3,4,9],'cs32312')
    print(my_fun_zip)
    for i in my_fun_zip:
        print(i)

    # filter
    my_fun_filter = my_fun('filter',None,['',0,False,1,3,4,9])
    print(my_fun_filter)
    for i in my_fun_filter:
        print(i)
    my_fun_filter = my_fun('filter',lambda x:x//2,['',0,False,1,3,4,9])
    print(my_fun_filter)
    for i in my_fun_filter:
        print(i)
