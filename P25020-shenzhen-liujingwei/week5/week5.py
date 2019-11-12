#1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random
alist = [1,2,3,4,5]
random.shuffle(alist)
print(alist)

# 2、已知仓库中有若干商品，以及相应库存，类似：
# 袜子，10
# 鞋子，20
# 拖鞋，30
# 项链，40
# 要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数

def getitem(n1=10,n2=20,n3=30,n4=40):
    str_a = 'a'*n1
    str_b = 'b'*n2
    str_c = 'c'*n3
    str_d = 'd'*n4
    str_all = str_a + str_b + str_c +str_d
    item = random.choice(str_all)
    if item == 'a':
        return 'socks'
    elif item == 'b':
        return 'shoes'
    elif item == 'c':
        return 'slippers'
    else:
        return 'ring'

item = getitem()
print(item)

