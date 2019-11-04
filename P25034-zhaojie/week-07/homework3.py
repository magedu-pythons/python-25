#!/usr/bin/env python
# encoding:utf-8
# file: homework3.py

# 3、以下代码输出什么，请解释原因(写到问题下方)

# 空列表乘5次只是把li[0]子列表的引用复制了5次
# 因此li的5个子列表实际上是同一个列表
# 使用id(li[N])查看子列表地址可以看到5个子列表地址是相同的
li = [[]] * 5

# 将会打印 [[10], [10], [10], [10], [10]]
# 原因如上，不管对哪个子列表追加，如li[2].append(10)，都在操作同一个子列表
li[0].append(10)
print(li)

# 将打印 [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
# 原因如上
li[1].append(20)
print(li)

# 这次是给列表li追加内容而不是子列表
# 将打印 [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
li.append(30)
print(li)
