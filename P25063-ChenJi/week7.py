# 本周作业，希望大家认真完成哦（11.4-11.10）
# 1、请将 "1,2,3"，变成 ["1","2","3"]
# 2、使用Python copy一个文件，从a目录,copy文件到b目录
# 3、以下代码输出什么，请解释原因(写到问题下方):
# li = [ [ ] ] * 5
# li[0].append(10)
# print(li)
# li[1].append(20)
# print(li)
# li.append(30)
# print(li)
#1
nums = "1,2,3"
num_list = nums.split(",")
print(num_list)
#2
import os
print(os.system('cp a/xxx.py b/xxx.py'))
#3
li = [[]] * 5
li[0].append(10)
print(li)
#li 是 list， 其中包含5个list指向同一内存地址
#li[0] 的值等价于 li[1] li[2] li[3] li[4]，指向同一内存地址
#[[10], [10], [10], [10], [10]]
li[1].append(20)
print(li)
#[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
li.append(30)
print(li)
#[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
