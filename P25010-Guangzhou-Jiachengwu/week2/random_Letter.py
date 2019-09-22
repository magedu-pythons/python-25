'''使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上'''
import random,string
words=string.octdigits+string.ascii_letters

Random_nums=[]
for i in range(200):
    Random_nums.append("".join(random.choices('0123456789'+Letters,k=6)))
print(Random_nums)   