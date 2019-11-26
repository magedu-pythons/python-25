#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None
str1 = 'abbcdghjk'
str2 = 'cdghh'
def Issubstr(str2,str1):
    len1 = len(str1)
    len2 = len(str2)
    if len2 > len1:
        return None
    else:
        for i in range(len1-len2):
            if str1[i:i+len2] == str2:
                return i
                break
        else:
            return None

print(Issubstr(str2,str1))

# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
lst = [1,5,2,7,4,9]
target = 6
def Addtwonum(lst,n):
    length = len(lst)
    for i in range(length):
        tmp = target - lst[i]
        for j in range(i+1,length):
            if lst[j] == tmp:
                return lst[i],lst[j]
                break
    else:
        return None

print(Addtwonum(lst,target))



