# 1. 字符串 str= 'reverse this string'， 请使用三种方法翻转字符串。
src = 'reverse this string'
print('翻转前：', src)

# 方法1
result = ''
for i in range(len(src)):
    result += src[-i - 1]
print('翻转后1', result)

# 方法2
result = ""
lst = []
for i in src:
    lst.append(i)
lst.reverse()
for j in lst:
    result += j
print('翻转后2', result)

# 方法3
# 未想到
# 除了列表有reverse()方法,字符串也有其自带的reversed()方法,可以去尝试一下.

# 2. 给出两个列表list1 = [1, 2, 3, 4, 5], list2=[3,4,7,8,9]，找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 7, 8, 9]
same_lst = []  # 存放相同元素
diff_lst = []  # 存放不同元素
# 方法1
# 先取两个列表中相同元素
for i in list1:
    for j in list2:
        if i == j:
            same_lst.append(i)

print('相同元素1', same_lst)
# 取list1中不同元素
for i in list1:
    if i not in same_lst:
        diff_lst.append(i)
# 取list2中不同元素
for i in list2:
    if i not in same_lst:
        diff_lst.append(i)

print('不同元素1', diff_lst)

# 方法2
s1 = set(list1)
s2 = set(list2)
# print(s1, s2)
same_set = s1 & s2
print('相同元素2', same_set)
diff_set = s1 ^ s2
print('不同元素2', diff_set)

# 方法3
same_lst = []
diff_lst = []
# print(same_lst,diff_lst)
for i in list1:
    if i in list2:
        same_lst.append(i)
    else:
        diff_lst.append(i)

print('相同元素3', same_lst)
for i in list2:
    if i not in same_lst:
        diff_lst.append(i)
print('不同元素3', diff_lst)

# 不错,集合,列表和循环都掌握的很好,后面要多加练习.老师提到的知识可以自己去尝试一下.
