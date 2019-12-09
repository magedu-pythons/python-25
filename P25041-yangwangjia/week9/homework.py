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
    return ''.join(map(str,[i for i in reversed(tmp)]))
# 这里可以直接使用join函数将reversed()返回的生成器拼接起来即可.

def fun3(tmp):
    tmp = [i for i in tmp]
    tmp.reverse()
    return ''.join(map(str,tmp))


# 测试函数
print(fun1(temp))
print(fun2(temp))
print(fun3(temp))


"""
题目：
    给出两个列表list1 = [1, 2, 3, 4, 5], list2=[3,4,7,8,9]，
    找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。

思路：
    方法一：
        set集合的并和差运算操作，找出相同和不同元素，
    方法二：
        for循环遍历操作，找出相同元素
        

"""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 7, 8, 9]

def fun1(lst1,lst2):
    
    temp1 = {i for i in lst1}
    temp2 = {i for i in lst2}
    
    newList = temp1 | temp2
    theSame = temp1 & temp2
    difference = newList - theSame
    return theSame,difference

def fun2(lst1,lst2):
    
    theSame=[]
    difference=[]
    
    for i in range(len(lst1)):
        flag = False
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                theSame.append(lst1[i])
                flag = True
        if not flag:
            difference.append(lst1[i])

    for i in lst2:
        if i not in theSame:
            difference.append(i)
            
    return theSame,difference


# 测试函数

print(fun1(list1,list2))
print(fun2(list1,list2))

# 不错,集合和集合解析式都用的很好,后面也可以继续,在学习到新的知识以后,再尝试迭代.
