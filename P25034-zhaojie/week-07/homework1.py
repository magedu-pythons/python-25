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
