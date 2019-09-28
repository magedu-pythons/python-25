def fib(n):
    if n < 3:
        return 1
    return fib(n-1)+fib(n-2)
i = 1
while fib(i) < 100:
     print(fib(i))
     i += 1