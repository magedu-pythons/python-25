#!/usr/bin/env python
# encoding:utf-8
# file: homework1.py

# 列表中找元素


def find1(lst, elem):
    """方法1：遍历
    """
    for i in lst:
        if elem == i:
            return 1
    else:
        return 0


def find2(lst, elem):
    """方法2：内置方法
    """
    return 1 if elem in lst else 0


if __name__ == '__main__':
    x = '123'
    a_list = [1, 2, 'a', '123', 2.2]
    b_list = [1, 2, 'a', '1234', 2.2]
    print(find1(a_list, x))
    print(find1(b_list, x))
    print(find2(a_list, x))
    print(find2(b_list, x))
