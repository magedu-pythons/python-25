#!/usr/bin/env python
# encoding:utf-8
# file: homework2.py

# 2. 给出两个列表list1=[1,2,3,4,5], list2=[3,4,7,8,9]，
# 找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。

# 方法1：遍历
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 7, 8, 9]
l1 = []
l2 = []
for i in list1:
    if i in list2:
        l1.append(i)
    else:
        l2.append(i)
for i in list2:
    if i not in l1:
        l2.append(i)
print(l1)
print(l2)
print()

# 方法2：集合操作 但是集合操作会去重
s1 = set(list1)
s2 = set(list2)
print(s1 & s2)
print(s1 ^ s2)
print()

# 方法3：排序后查找交集的起点和终点索引
list1.sort()
list2.sort()
l1_len = len(list1)
l2_len = len(list2)
start, end = 0, 0
for i in range(l1_len):
    if list1[i] == list2[0]:
        # list1的交集元素起点
        start = i
        for j in range(l2_len):
            if start + j < l1_len and list1[start + j] != list2[j]:
                # list2的交集元素终点+1
                end = j
                break
            elif start + j >= l1_len:
                end = j
                break
        break
print(list1[start:start + end])
print(list1[:start] + list1[start + end:] + list2[end:])
