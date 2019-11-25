# 给出两个列表list1 = [1, 2, 3, 4, 5], list2=[3,4,7,8,9]，
# 找出列表中相同和不同的元素，使用两种（包含两种）以上方法实现。

# 方法1：
list1 = [1, 2, 3, 4, 5]
list2=[3,4,7,8,9]

s1=set(list1)
s2=set(list2)

print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

# 方法2：
list1 = [1,2,3,4,5]
list2 = [3,4,7,8,9]

s1=set(list1)
s2=set(list2)

def sa_df(set1:set,set2:set,sa=[],di=[]):
    for i in set1:
        sa.append(i) if i in set2 else di.append(i)
    return set(sa),set(di)

sa_df(s1,s2)
glsa,gldf=sa_df(s2,s1)
print(glsa,gldf)


# 第一种方法使用的很不错,
# 第二个方法建议在1个函数里完成整个功能,而不是一个函数操作两遍.
