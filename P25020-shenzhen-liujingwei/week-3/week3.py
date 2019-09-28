#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
s = ['a','h',4,6,'mn','x',10,56,98]
x = '1'
flag = 0
for i in s:
    if x == i:
        flag = 1
        break
else:
    flag = 0
print(flag)

#任一个英文的纯文本文件，统计其中的单词出现的个数
file = 'D:/python/homework/week3/test.txt'
with open(file,'r') as f:
    lst = f.readlines()
wordnum = 0
print(lst)
for s in lst:
    tmp = s.strip().split()
    for word in tmp:
        if word[0].isalpha() or word[-1].isalpha():  #去掉非单词
            wordnum += 1
        else:
            continue
print(wordnum)

