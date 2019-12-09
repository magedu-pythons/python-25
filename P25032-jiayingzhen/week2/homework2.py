# 第二周作业
# 1、打印出100以内的斐波那契数列，使用2种方法实现
# 方法一. for循环

f1 =1
f2 =1
print(f1)
print(f2)
for fn in range(2, 101):
    if fn == f2+f1:
        print(fn)
        f1, f2 = f2, fn
# 方法二，while循环：

f1 = 0
f2 = 1
fn = 1
while fn < 100:
    print(fn)
    fn = f2 + f1
    f1,f2 = f2,fn


# 2、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random
list1 = []
list1 = list(set(list1))
while  5  > len(list1)-1:
    list1.append(random.randint(0, 200))
print(sorted(list1))
