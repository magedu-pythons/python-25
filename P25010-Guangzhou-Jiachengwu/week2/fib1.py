'''打印出100以内的斐波那契数列，使用2种方法实现'''
n=0
a=1
b=1
print(a)
print(b)
while True:
    n=a+b
    if n > 100: break
    a=b
    b=n
    print(n)