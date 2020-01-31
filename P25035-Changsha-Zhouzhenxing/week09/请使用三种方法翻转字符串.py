# 1. 字符串 str= 'reverse this string'， 请使用三种方法翻转字符串。

# 第一种方法使用reversed
str= 'reverse this string'
r = reversed(str)
str_new = ''.join(r)
print(str_new)

# 第二种方法使用反向切片
str= 'reverse this string'
length = len(str)
str_new = str[-1:-length-1:-1]
print(str_new)

# 第三种方法使用列表解析式
str= 'reverse this string'
length = len(str)
lst = [str[i] for i in range(length-1, -1, -1)]
str_new = ''.join(lst)
print(str_new)