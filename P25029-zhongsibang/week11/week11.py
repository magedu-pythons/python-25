#自己实现python自带的map、zip、filter函数

#map
def MyMap(fn,*iterables):
    shortest = min(len(i) for i in iterables)
    for i in range(shortest):
        yield fn(*tuple(j[i] for j in iterables))

#MyMap测试
def add(a,b,c):
    return a+b+c

for i in MyMap(add,(1, 2, 3,4), [4, 5, 6], (1,2)):
    print(i)
a = MyMap(add,(1, 2, 3,4), [4, 5, 6], (1,2))
print(next(a))
print(next(a))


#filter
def MyFilter(fn,iterables):
    for i in iterables:
        if fn(i):
            yield i
#MyFilter测试
print(list(MyFilter(lambda x : x%3==0,(1,9,55,150,-3,78,28,123))))


#zip
def MyZip(*iterables):
    shortest = min(len(i) for i in iterables)
    for i in range(shortest):
        yield tuple(j[i] for j in iterables)

#MyZip测试
x = [1, 2, 3]
y = [4, 5, 6]
zipped = MyZip(x, y)
print(list(zipped))

# 实现的非常简洁, 元组解析式用的非常好. 但是基本的异常情况没有考虑到.不知道你有没有学习到异常这一节.
# 但是基本的错误情况是需要考虑一下的,例如传进来的对象不是一个可迭代对象,你这里的实现会出现什么样的情况,可以测试一下?
