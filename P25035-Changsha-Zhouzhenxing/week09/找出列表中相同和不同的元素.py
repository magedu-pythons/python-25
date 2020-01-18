# 2. 给出两个列表list1 = [1, 2, 3, 4, 5], list2=[3,4,7,8,9]，找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。

list1 = [1, 2, 3, 4, 5]
list2=[3, 4, 7, 8, 9]

# 第一种方法使用集合
s1 = set(list1)
s2 = set(list2)

print('相同的元素:', s1 & s2) #相同的元素
print('不相同的元素:', s1 ^ s2) #不相同的元素


# 第二种方法
# 构造一个新的10个0的列表lst，分别循环list1、list2，将值对应到lst的索引，lst的索引上的值+1
# 最后遍历lst，如果值>1则索引值就是list1、list2的公共元素，如果=1则是不同的元素
lst = [0] * 10

for item1 in list1:
    lst[item1] += 1

for item1 in list2:
        lst[item1] += 1

comm = []
differ = []
for i in range(len(lst)):
    if lst[i] > 1:
        comm.append(i)
    elif lst[i] == 1:
        differ.append(i)

print('相同的元素:', comm) #相同的元素
print('不相同的元素:', differ) #不相同的元素