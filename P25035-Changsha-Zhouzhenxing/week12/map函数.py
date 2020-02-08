# map函数
def mymap(func, iter):

 for val in iter:
  ret = func(val)
  yield ret
  
  

# 调用
g = (mymap(str, [1, 2]))
print(next(g))
print(next(g))