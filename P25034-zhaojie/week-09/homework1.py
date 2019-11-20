#!/usr/bin/env python
# encoding:utf-8
# file: homework1.py

# 1. 字符串 str='reverse this string'，请使用三种方法翻转字符串。

# 方法1：反向迭代输出
s = 'reverse this string'
s_tmp = ''
s_len = len(s)
for i in range(-1, -s_len - 1, -1):
    s_tmp += s[i]
print(s_tmp)

# 方法2：类似入栈出栈
s_tmp = ''
for c in s:
    s_tmp += c
print(s_tmp[::-1])

# 方法3：列表反转
s_tmp = list(s)
s_tmp.reverse()
print(''.join(s_tmp))

# 方法4：索引特性
print(s[::-1])
