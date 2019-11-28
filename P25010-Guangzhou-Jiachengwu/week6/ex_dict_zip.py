# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

tup1=(('a'),('b'))
tup2=(('c'),('d'))

# 写法一
def tupdic(args):
    a=list()
    for x in args:
        a.append(dict((x,)))
    return a

a=tupdic(zip(tup1,tup2))
print(a)


# 变为匿名函数
a=(lambda args : [dict((x,)) for x in args]) (zip(tup1,tup2))   
# zip(tup1,tup2) => ('a','c'),('b','d')，塞进去强行把他变成二元组(,)=>(('a','c'),)
print(a)

a=(lambda args : [{i,j} for i,j in args]) (zip(tup1,tup2))
print(a)


