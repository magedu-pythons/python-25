from functools import wraps


"""这次处理string问题中还是少量调用了系统的函数如使用到了系统提供的装饰器wraps修改装饰器名称，帮组文档；同时还用到dict.get()获取传参；元祖索引....

思路：
    1. 使用列表解析式加列表的索引实现字符串翻转
    2. for循环遍历处理index返回
    3. chr()比较字符串大小进行转换
       chr(65)~chr(90)：A-Z
       chr(97)~chr(122)：a-z
       ord()返回字符串的数字值
       isinstance 判断是否是str类型
"""


def my_sort(fn):
    @wraps(fn)  # 修改装饰器的名字和参数为调用函数的名字和帮助文档
    def _my_sort(*args, **kwargs):
        # 接收传入的参数
        source = fn(*args, **kwargs)

        # 接收关键字参数，在这接收处理index、reverse、upper、lower、find参数
        reverse = source[1].get('reverse', False)
        index = source[1].get('index', None)
        find = source[1].get('find', None)
        if index and find:
            return "Error! Can't do this Operation, index and find!"
        upper = source[1].get('upper', None)
        lower = source[1].get('lower', None)
        if upper and lower:
            return "Error! Can't do this Operation, upper and lower!"
        # 接收要处理的字符串参数
        # 要处理的字符串超过一个拒绝处理·~·
        if len(source[0]) > 1:
            return 'Error! function took 1 args but give 2'
        # 将接受的字符串转换成列表开始处理
        source = list(source[0][0])
        length = len(source)

        '''使用列表解析式加列表的索引实现字符串翻转'''
        if reverse:
            source = [source[-i - 1] for i in range(length)]
        source = [source[i] for i in range(length)]
        # 组装字符串
        temp = ''
        for i in source:
            temp += i
        temp = [temp, ]

        '''处理index and find'''
        if index or find:
            def _search(search_name, search_str):
                print(search_name, search_str)
                nonlocal temp
                count = 0
                flag = False
                temp = temp[0]
                for i in temp:
                    if i == search_str:
                        temp = [temp, {search_name: count}]
                        flag = True
                        break
                    else:
                        count += 1
                if not flag:
                    if search_name == index:
                        temp = [temp, {search_name: search_str + ' Not found'}]
                    else:
                        temp = [temp, {search_name: '-1'}]

            _search('index', index) if index else _search('find', find)

        '''处理upper and lower'''
        if upper or lower:
            """print(temp[0])  # 待处理字符串,print(temp[1])  # 函数返回值"""
            tmp = ''
            for i in temp[0]:
                if isinstance(i, str):
                    if upper:
                        if 96 < ord(i) < 123:
                            i = chr(ord(i) - 97 + 65)
                    elif lower:
                        if 64 < ord(i) < 91:
                            i = chr(ord(i) - 65 + 97)
                tmp += i
            temp[0] = tmp

        return temp

    return _my_sort


@my_sort
def fun_string(*args, **kwargs):
    """实现string类的核心代码,当前仅支持传入字符串，请使用位子参数传参，且位置参数仅支持接收一个参数。函数返回一个列表。

    reverse:字符串翻转，默认字符串为正序打印
    upper:返回转换后的大写字符串
    lower:返回转换后的小写字符串
    index:返回字符串索引，找到返回元素第一次出现的索引，否则返回Error！
    find:查找元素是否在字符串中，找到返回元素第一次出现的索引，否则返回-1

    调用须知：
        upper和lower不能同时调用，否者报Error！
        index和find不能同时调用，否则报Error！
        此函数调用后返回一个列表，列表有两个参数，参数一是转换后的字符串，参数二返回find或index的结果，若不调用不反回参数二。
    """
    temp = args, kwargs
    return temp


if __name__ == "__main__":
    # 帮助文档
    print("function help documents\n{}\n\n\n".format('-' * 24))
    print('function name: {}\n'.format(fun_string.__name__))
    print("function mean：\n{}".format(fun_string.__doc__))

    print("{}\n\n\n".format('=' * 125))
    print(fun_string('abcd', reverse=True))

    print(fun_string('abcd', index='csa'))
    print(fun_string('abcd', index='a'))

    print(fun_string('1w23', index='csa', upper=True))
    print(fun_string('JIUXAHIU', upper=True, lower=True))

    print(fun_string('JIUXAT1234XxssHIU', lower=True))
    print(fun_string('JIUXAT1234XxssHIU', index='123', find='1'))

    print(fun_string('1JIUXAT1234XxssHIU', find='0'))
    print(fun_string('1JIUXAT1234XxssHIU', find='1'))

