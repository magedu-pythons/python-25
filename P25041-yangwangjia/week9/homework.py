"""
题目：
    字符串 str= 'reverse this string'， 请使用三种方法翻转字符串。
思路：
    使用字符串切片
    使用reversed()函数
    使用列表的reverse方法
"""
temp = 'reverse this string'

def fun1(tmp):
    return tmp[::-1]

def fun2(tmp):
    return [i for i in reversed(tmp)]

def fun3(tmp):
    tmp = [i for i in tmp]
    tmp.reverse()
    return tmp
# 第二种和第三种方法别忘了把列表里的字符拼接了返回.

# 测试函数

# fun1(temp)
# fun2(temp)
# fun3(temp)


"""
题目：
    给出两个列表list1 = [1, 2, 3, 4, 5], list2=[3,4,7,8,9]，
    找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。

思路：
    set集合的in操作
    for循环遍历操作

"""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 7, 8, 9]

def fun1(lst1,lst2):
    temp = {i for i in lst2}
    return [i for i in lst1 if i in temp]

def fun2(lst1,lst2):
    return [i for i in lst1 if i in lst2]


# 测试函数

# fun1(list1,list2)
# fun2(list1,list2)

#第二种方法的思路是对的,但是具体的实现错了, 一次循环是没法找出两个列表里的不同元素的,可以再尝试一下.
