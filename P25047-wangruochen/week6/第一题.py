old_1 = (('a'),('b'))
old_2 = (('c'),('d'))
old = zip(old_1,old_2)
new = list(map(lambda tup:{tup[0],tup[1]},old))
print(new)

# 这里得出来的结果并不是想要的,想要的是一个字典,如果想要字典,那么就构建字典,构建字典的匿名函数一般格式是:
# lambda x,y: {x:y}
# 然后可以使用python的组合函数,将这两个元组应用这个匿名函数,同学可以尝试一下.
