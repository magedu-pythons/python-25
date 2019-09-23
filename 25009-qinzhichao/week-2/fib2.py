def fib(a,b):
    return a+b
a=0
b=1
print(a)
print(b)
for c in range(0,100):
    c=a+b
    if c>100:
        break
    print(c)
    a=b
    b=c
