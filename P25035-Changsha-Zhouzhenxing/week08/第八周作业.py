第八周作业

1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。

# 判断字符串str2是否是str1的子串
def index(str1, str2):
    str2_len = len(str2)
    length = len(s1)
    
    for i in range(0, length):
       if str1[i:(str2_len + i)] == str2:
            return i
    else:
       return None


# 调用示例
s1 = 'ADCF'
s2 = 'DC'

idx = index(s1, s2)
if idx == None:
    print('None')
else:
    print(idx)


2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

# 查找列表lst中和为total的两个数
# 返回：一个列表，元素为和为total的两个数组成的元组
def fn(lst, total):
    d = {} #定义一个字典，保存查找过的数据，默认值为0；如果找到两个数和为total时，将K、V设置为这两个数
    lst_ret = [] # 保存返回值
    for item in lst:
        if total - item in d:
            d[total - item] = item
            lst_ret.append((total - item, item))
        else:
            d[item] = 0
            
    return lst_ret


# 调用示例
lst =[1,5,2,7,4,9]
print(fn(lst, 11))
        
