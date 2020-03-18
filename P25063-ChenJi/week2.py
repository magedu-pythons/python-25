#打印出100以内的斐波那契数列
def fib100():
    a, b = 1, 1
    print(b)
    while b < 100:
        print(b)
        a, b = b, a+b
fib100()


def fib100_2():
    def fib(n):
        if n < 3:
            return 1
        return fib(n-1)+fib(n-2)
    i = 1
    res = fib(i)
    while res < 100:
        print(res)
        i = i + 1
        res = fib(i)

fib100_2()


#使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random, string
asc = string.ascii_letters + string.digits
codes = set()
#print(random.choices(asc, k=10))
while len(codes) < 200:
    codes.add("".join(random.choices(asc, k=10)))
print(codes, len(codes))

