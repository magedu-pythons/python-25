from functools import wraps
import inspect


def check(fn):
    @wraps(fn)
    def _wrapper(*args, **kwargs):
        """ 参数类型校验装饰器

        :param args:
        :param kwargs:
        :return:
        """
        sig = inspect.signature(fn)  # 获取函数签名
        params = sig.parameters
        values = list(params.values())

        # 函数调用参数和函数声明类型校验
        # 位置参数校验
        for i, p in enumerate(args):
            param = values[i]
            if param.annotation is not param.empty and not isinstance(p, param.annotation):
                raise ValueError(p, 'not', values[i].annotation)

        # 关键字参数校验
        for k, v in kwargs.items():
            if params[k].annotation is not inspect._empty and not isinstance(v, params[k].annotation):
                raise ValueError(k, v, 'not', params[k].annotation)

        # 参数校验结束调用函数
        ret = fn(*args, **kwargs)

        return ret
    return _wrapper


"""
不使用系统函数，自己实现一个string类，实现基本的字符串翻转reverse，索引 index，大写upper，小写lower，查找find等功能。
"""


@check
def my_str(src: str, *args, reverse: bool=False, index: str=None,
           find: str=None, upper: bool=False, lower: bool=False, **kwargs):

    # 获取参数
    def param():
        dic = dict()
        if reverse:
            dic['reverse'] = True
        if index:
            dic['index'] = index
        if find:
            dic['find'] = find
        if upper:
            dic['upper'] = upper
        if lower:
            dic['lower'] = lower
        for k, v in kwargs.items():
            dic[k] = v
        return dic

    # 反转函数
    def _reverse():
        return ''.join([src[i] for i in range(len(src)-1, -1, -1)])

    def _found(types: str, sub: str):
        """ 查找函数

        :param types: 调用函数类型
        :param sub: 待查找字符串
        :return: 字符串
        """
        flag = False
        for i in range(len(src)):
            offset = len(sub)
            if sub == src[i:i+offset]:
                flag = True
                return i
        if not False:
            if types == 'index':
                raise ValueError('substring not found')
            else:
                return -1

    # 大小写转换
    def _upper():
        ret = ''
        for i in src:
            if 96 < ord(i) < 123:
                ret += chr(ord(i) - 97 + 65)
            else:
                ret += i
        return ret

    def _lower():
        _lower_ret = ''
        for i in src:
            if 65 < ord(i) < 90:
                _lower_ret += chr(ord(i) - 65 + 97)
            else:
                _lower_ret += i
        return _lower_ret

    # 调用参数函数,获取参数字典
    params = param()

    # 是否翻转
    if params.get('reverse'):
        src = _reverse()

    # 调用查找方法
    _f_index = params.get('index')
    _f_found = params.get('find')
    if _f_index or _f_found:
        if _f_index:
            _found_ret = _found('index', _f_index)
        else:
            _found_ret = _found('find', _f_found)

        return _found_ret

    # 调用upper
    if params.get('upper'):
        return _upper()

    # 调用lower
    if params.get('lower'):
        return _lower()

    return src


if __name__ == "__main__":
    # 调用示例
    print(my_str('ab23GtD4drds',lower=True))
    print(my_str('ab23GtD4drds', upper=True))
    print(my_str('ab23GtD4drds', index='GtD'))
    # print(my_str('ab23GtD4drds', index='GtDcscas'))
    print(my_str('ab23GtD4drds', find='GtD'))
    print(my_str('ab23GtD4drds', find='GtDcscas'))
    print(my_str('ab23GtD4drds', reverse=True))
