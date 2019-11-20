# 字符串 str= 'reverse this string'， 请使用三种方法翻转字符串。

# 方法1：
str= 'reverse this string'
print(str[::-1])

# 方法2：
str= 'reverse this string'
length=len(str)
str1=''

for i in range(length,0,-1):
    str1+=str[i-1]
print(str1)

# 方法3：
str= 'reverse this string'
str3=reversed(str)
str4=''
for i in str3:
    str4+=i
print(str4)
