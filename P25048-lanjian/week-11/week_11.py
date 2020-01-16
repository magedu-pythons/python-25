# 自定义map函数
def my_map(function, *iterable, **kwiterable):
    # 参数合法检验
    if function is None:
        print('函数不能为None')
        return

    totallist = []  # 放置所有参数的集合
    # 添加位置参数
    for i in iterable:
        totallist.append(i)

    # 添加关键字参数
    for _, v in kwiterable.items():
        if v is not None and len(v) > 0:
            totallist.append(v)

    # print('totallist:', totallist)
    if len(totallist) == 0:
        print('输入的参数不能为空')
        return
    # 获取最短集合长度
    minlen = len(totallist[0])
    for i in range(len(totallist)):
        le = len(totallist[i])
        if le < minlen:
            minlen = le

    # 组合所有可迭代对象
    result = []
    for i in range(minlen):
        args = []  # 组合参数集合
        for lst in totallist:
            pos_arg = lst[i]
            args.append(pos_arg)

        res = function(*args)
        result.append(res)

    return result


# 自定义zip函数
def my_zip(*iterable):
    if iterable is None or len(iterable) == 0:
        print('请输入可迭代参数')
        return

    result = []
    minlen = len(iterable[0])  # 最短长度
    for i in iterable:
        le = len(i)
        if le < minlen:
            minlen = le

    for i in range(minlen):
        t = []
        for it in iterable:
            t.append(it[i])
        result.append(tuple(t))

    return result


# 自定义filter函数
def my_filter(function, iterable):
    for x in iterable:
        if callable(function):  # 是函数，则调用
            flag = function(x)
            if flag:
                yield x
        else:  # 不是函数，则取非空元素
            if x:
                yield x
