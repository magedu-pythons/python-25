'''打印出100以内的斐波那契数列，使用2种方法实现'''
n=0
a=1
b=1
print(a)
print(b)
while n<100:
    print(n)
    n=a+b
    a,b=b,n