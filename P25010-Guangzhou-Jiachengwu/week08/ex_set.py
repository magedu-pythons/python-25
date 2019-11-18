# 实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。


def str1str2 (str1:str,str2:str):
    rindex=str1.find(str2)
    if rindex >=0:
        return rindex
    else:
        return None

s1='12345'
s2='234'
print(str1str2(s1,s2))