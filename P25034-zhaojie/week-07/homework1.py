#!/usr/bin/env python
# encoding:utf-8
# file: homework1.py

# 1、请将 "1,2,3"，变成 ["1","2","3"]

# 方法1
a = '1,2,3'
print(a.split(','))

# 方法2 遍历一下
a = '1,2,3'
sep = ','
result = []
for i in range(len(a)):
    if a[i] == sep:
        continue
    result.append(a[i])
print(result)

"""
第一种方法比较简单，略过。
第二种方法，遍历的思路是对的，但是只针对本题给出的示例字符串有效，如果将字符串改成下面的样式：
b = '1,23,45,678'
c = '1, 23, 4, 5'
该怎么遍历呢？可以尝试迭代一下。
"""

# 优化版，能处理空格等，只用一个循环
a = ',1,23,   456 , ab  c,,,'
sep = '\t ,'
tmp_str = ''
result = []
for i in a:
    if i in sep:
        if tmp_str:
            result.append(tmp_str)
        tmp_str = ''
        continue
    tmp_str += i
print(result)
