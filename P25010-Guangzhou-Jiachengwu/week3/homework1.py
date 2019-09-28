# 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
import random,string

string.octdigits
words=string.octdigits+string.ascii_letters

n=int(input("输入一个数字n在0到100内生成n个随机数的列表："))

Random_nums=[]
for i in range(n):
    Random_nums.append("".join(random.choices(words,k=6)))
    
print("\n{}".format(Random_nums))

m=input("\n输入x，找出x元素是否在列表里面，如果存在返回1，不存在返回0: " )

length=len(Random_nums)//2

if m in Random_nums:
    RE=1
else:
    RE=0

print(RE)