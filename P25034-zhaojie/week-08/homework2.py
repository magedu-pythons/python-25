#!/usr/bin/env python
# encoding:utf-8
# file: homework2.py

# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst = [1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11


# 方法1：暴力法 迭代全部
def find_val(li, val):
    # li 给定的整数列表
    # val 指定值
    result = []
    len_li = len(li)
    for i in range(len_li):
        for j in range(i + 1, len_li):
            if li[j] + li[i] == val:
                # 找出它们的索引值
                result.append((i, j))
    return result


if __name__ == '__main__':
    lst = [1, 5, 2, 7, 4, 9]
    num = 11
    print(find_val(lst, num))
