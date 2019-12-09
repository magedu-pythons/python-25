#!/usr/bin/env python
# encoding:utf-8
# file: homework1.py

# 现有两元组 (('a'),('b')),(('c'),('d'))，请使用Python中的匿名函数生成列表 [{'a':'c'},{'b':'d'}]

t1 = (('a',), ('b',))
t2 = (('c',), ('d',))

# 调用方法1
f = lambda a, b: [{t1[0][0]: t2[0][0]}, {t1[1][0]: t2[1][0]}]
print(f(t1, t2))

# 调用方法2
print((lambda a, b: [{t1[0][0]: t2[0][0]}, {t1[1][0]: t2[1][0]}])(t1, t2))
