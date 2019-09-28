#pyenv，jupyter
已经搭建好pyenv
global：全局生效，影响其他使用
local：对当前目录生效
shell：对当前shell生效，退出重新登录失效

jupyter已安装完成
pip install jupyter
jupyter notebook --ip=0.0.0.0 --no-browser --allow-root

#下面是作业要求的代码，基础差，想了半天，写了N久o(╥﹏╥)o

o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o

#斐波那契数列
f(1)=1
f(2)=1
f(n)=f(n-1)+f(n-2)

a = 1
b = 1
while True:
    c = a + b
    a = b 
    b = c
    if c == 2:
        print(1)
        print(1)
        print(c)
    elif c < 100:
        print(c)
    else:
        break

a = 1
b = 1
for i in range(3,1000):
    c = a + b
    a = b
    b = c
    if i == 3:
        print(1)
        print(1)
        print(c)
    else:
        if c < 100:
            print(c)
        else:
            break



#随机数
import random
import string

key = set()
while True:
    ran = ''.join(random.sample(string.ascii_letters + string.digits, 12))
    key.add(ran)
    if len(key) <= 199:
    	continue
    elif len(key) == 200:
    	for i in list(key):
    	    print(i)
    else:
        break


