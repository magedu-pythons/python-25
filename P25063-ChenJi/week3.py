#1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
lst = ['a', 'b', 'c', 'x', 'd']
def findx():
    for ch in lst:
        if ch == 'x':
            return 1
    else:
        return 0
print(findx())

# 如果x是一个随机字符呢？代码该怎么修改？

#2、任一个英文的纯文本文件，统计其中的单词出现的个数
import string
word_dict = {}
with open('english') as f:
    txt = f.read()
for word in txt.split(" "):
    word_dict[word.strip(string.punctuation)] = word_dict.get(word.strip(string.punctuation), 0) + 1
print(word_dict)

# 只使用空格来分隔字符串，忽略了英文里面以, . ! ? 等各种标点符号结尾的情况。
