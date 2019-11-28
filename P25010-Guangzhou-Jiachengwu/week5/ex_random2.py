# 已知仓库中有若干商品，以及相应库存，类似：
# 袜子，10
# 鞋子，20
# 拖鞋，30
# 项链，40
# 要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数

import random

def randpick(n):
    socks = ['wz'] * 10 * n
    shoes = ['xz'] * 20 * n
    slippers = ['tx'] * 30 * n
    necklace = ['xl'] * 40 * n
    for_all = socks + shoes + slippers + necklace

    count={'wz':0,'xz':0,'tx':0,'xl':0}
    for i in random.sample(for_all,n):
        count[i]+=1

    return count



a=randpick(10)
print(a)
a=randpick(210)
print(a)
a=randpick(230)
print(a)
a=randpick(440)
print(a)
a=randpick(500)
print(a)
a=randpick(5000)
print(a)