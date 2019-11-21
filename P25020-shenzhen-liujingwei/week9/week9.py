# 1. 字符串 str= 'reverse this string'， 请使用三种方法翻转字符串。
str1 = 'reverse this string'
#方法1：
ret1 = str1[::-1]
print(ret1)
#方法2：
ret2 = ''
for i in range(len(str1)-1,-1,-1):
    ret2 += str1[i]
print(ret2)
#方法3：
ret3 = ''.join(list(reversed(str1)))
print(ret3)
# 2. 给出两个列表list1 = [1, 2, 3, 4, 5], list2=[3,4,7,8,9]，找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。
#方法1：集合
lst1 = [1,2,3,4,5]
lst2 = [3,4,7,8,9]
set1 = set(lst1)
set2 = set(lst2)
print('1.相同的元素有：',set1&set2)
print('1.不同的元素有：',set1.symmetric_difference(set2))
#方法2：列表
lst_all = lst1+lst2
length = len(lst_all)
lst_com = []
lst_diff = []
status = [0]*length
for i in range(length):
    if status[i] == 1:
        continue
    for j in range(i+1,length):
        if status[j] == 1:
            continue
        if lst_all[i] == lst_all[j]:
            lst_com.append(lst_all[i])
            status[j] = 1
            status[i] = 1
for k in range(length):
    if status[k] == 0:
        lst_diff.append(lst_all[k])

print('2.相同的元素有：',lst_com)
print('2.不同的元素有：',lst_diff)

#方法3：字典
lst_com1 = []
lst_diff1 = []
lst_all = lst1+lst2
length = len(lst_all)
d = {}
for i in range(length):
    if d.get(lst_all[i],1):
        d[lst_all[i]] = 0
    else:
        lst_com1.append(lst_all[i])
        d[lst_all[i]] = 1
for k,v in d.items():
    if v == 0:
        lst_diff1.append(k)

print('3.相同的元素有：',lst_com1)
print('3.不同的元素有：',lst_diff1)



