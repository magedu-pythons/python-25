"""
两种方法实现斐波那契数列
"""

# 方法一、list列表实现

print("方法一>>\n")
fibn = 0
fib = 0
l=[]
i=0
while True:
    if fibn<100:
        if i==0:
            fib=0
            fibn=fib
            l.append(fib)
        elif i==1:
            fib=1
            fibn=fib
            l.append(fib)
        elif i==2:
            fib=1
            fibn=fib
            l.append(fib)
        else:
            fib=fibn
            l.append(fib)
        fibn+=l[i-1]
        print('fib '+str(i)+' =',fib)
        i+=1
    else:
        break

# 方法二、a、b、c交换实现


print("方法二>>\n")
a=0
b=1
i=2
print("fib 0 = 0")

print("fib 1 = 1")
while True:
    c=a+b
    
    if c>100:
        break
    print('fib '+str(i)+" = "+str(c))
    a=b
    b=c
    i+=1






"""
使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

"""


import uuid
l_t=[]
for i in range(200):
    token=uuid.uuid4()
    l_t.append(str(token))
print(l_t)
