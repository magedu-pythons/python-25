# 打印出100以内的斐波那契数列，使用2种方法实现
#第一种
a = 1
b = 1
print(a,b,sep=" ",end="")
c = a + b
while c < 100:
    print(" ",c,end="")
    a = c
    c = c + b
    b = a

# 第二种
print("\n")
a = 1
b = 1
while True:
    c = a + b
    if c == 2:
        print('{} {} {}'.format(a, b,c), end="")
    elif c <= 100:
        print(" ",c,end="")
    else:
        break

    a = b
    b = c

#使用Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random
lis = []
while True:
    b = random.randint(6,9)
    a = random.randint(10000,10**b)
    if a in lis:
        continue
    else:
        lis.append(a)
        if len(lis) >= 200:
            break;
print(lis)





