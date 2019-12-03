# 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
list1 = list(range(1,20))
a = int(input(">>"))
if a in list1:
    print( True )
else:
    print(False)

print('List: {}'.format(list1))

