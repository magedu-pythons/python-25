#1打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random
alist=[1,2,3,4,5]
random.shuffle(alist)
print(alist)

# 2已知仓库中有若干商品，以及相应库存，类似：
# 袜子，10
# 鞋子，20
# 拖鞋，30
# 项链，40
# 要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
store_dict = {'socker': 10, 'shoes': 20, 'slippers': 30, 'necklace': 40}
def random_good():
    all = sum(store_dict.values())
    cur_dict = {}
    val = 0
    for k,v in store_dict.items():
        print(k, ' probability', v/all)
        cur_dict[k] = set(range(val, val+v))
        val = val + v
    #print(cur_dict)
    num = random.randrange(0, all)
    for k,v in cur_dict.items():
        if num in v:
            store_dict[k] -= 1
            return k

for i in range(10):
    print(random_good())

    
# 这个题目最终要求达到的效果是，我从里面取100次，或者1000次，最终的结果中，取出来各项商品的数量和它的比例应该是符合的
# 而不是说每次取完以后都要重新计算它的比例。
