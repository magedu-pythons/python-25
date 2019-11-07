#!/usr/bin/env python
# encoding:utf-8
# file: homework2.py

# 2、使用Python copy一个文件，从a目录,copy文件到b目录
# 用Python复制文件的9个方法：https://zhuanlan.zhihu.com/p/35725217

source = input("Input source file absolute path: ")
target = input("Input destination file absolute path: ")
with open(source, 'rb') as fd_source:
    tmp = fd_source.read()
    with open(target, 'wb') as fd_target:
        fd_target.write(tmp)
