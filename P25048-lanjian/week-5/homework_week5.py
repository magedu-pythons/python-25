# 1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random

alist = [1, 2, 3, 4, 5]
print('打乱前：', alist)
random.shuffle(alist)
print('打乱后：', alist)

'''2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
'''


def random_take():
    # goods = {'袜子': 10, '鞋子': 20, '拖鞋': 30, '项链': 40}
    # 随机获取商品下标
    index = random.randrange(0, 100, 10)
    print('商品下标=', index)
    result = dict()
    if index >= 60:  # 60~100是项链
        result.setdefault('项链', 40)
    elif index >= 30:  # 30~60是拖鞋
        result.setdefault('拖鞋', 30)
    elif index >= 10:  # 10~30是鞋子
        result.setdefault('鞋子', 20)
    elif index >= 0:  # 0~9是袜子
        result.setdefault('袜子', 10)

    print('找到商品：', result)


random_take()
