# 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
"""
不建议使用列表的in方法该方法的时间复杂度为O(n),会随着问题规模的增长耗时越来越长
如果非要用in方法建议使用dict字典或set集合
"""
import random

nums = [random.randrange(1,21) for i in range(random.randrange(1,11))]  # [1-10]以内任意长度一个列表，元素为[1-20]的随机数
print(nums)
usr_in = int((input("please input a keyword:\n")).strip())  # 去除输入的前后空格后转换成int类型

if usr_in in nums:
    print(1)
else:
    print(0)



# 任一个英文的纯文本文件，统计其中的单词出现的个数。
usr_in = "Bullying Drama “Better Days” Makes Unexpected Comeback from Censorship"

count = 0
for i in usr_in:
    if i == " ":
        count+=1
print(count)
