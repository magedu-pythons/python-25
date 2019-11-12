#!/usr/bin/env python
# encoding:utf-8
# file: homework1.py

# 1、实现一个函数用于判断字符串str2是否是str1的子串。
# 如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。


# 方法1：依次比较 效率低
def str_search(s, sub):
    # s为目标字符串 sub为子字符串
    len_sub = len(sub)
    len_s = len(s)
    pos = None
    for i in range(len_s):
        for j in range(len_sub):
            if sub[j] != s[i + j]:
                break
        else:
            # 子字符串不为空则对应for循环已正常迭代完毕
            if len_sub > 0:
                return i
    return pos


# 方法2：使用内置方法
def str_search2(s, p):
    return s.find(p)


# 其他高效算法
# TODO 字符串匹配算法 RF(Rabin-Karp) KMP BM Sunday 实现

if __name__ == '__main__':
    tmp_s = 'abcav123av.56, 24avx'
    tmp_p = '23'
    print(str_search(tmp_s, tmp_p))
    print(str_search2(tmp_s, tmp_p))
