1、搭建好pytenv环境，理解local、global、shell3种方式区别，安装部署完成jupyter并运行
local  对当前的目录进行python版本的设定，当前目录下的子目录会继承这个设定。
global 全局修改python版本。
shell 只对当前会话的shell做设定，当退出当前会话的shell，这个设定也就失效了。
2、打印出100以内的斐波那契数列，使用2种方法实现
第一种：
#fib
a=0
b=1
print(0,a)
print(1,b)
i = 2
while True:
    c = a + b 
    if c > 100:
        break
    print(i , c)
    a = b 
    b = c
    i += 1
第二种：不会

3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
不会