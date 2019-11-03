# 打乱一个排好序的list对象alist，alist=[1,2,3,4,5] 
"""
random的shuffle()方法对原列表顺序打乱
"""
import random

alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)


















# -------------------------------------------------------------------

import random
"""
已知仓库中有若干商品，以及相应库存，类似：

袜子，10

鞋子，20

拖鞋，30

项链，40

要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数 
"""
def fun_res():
#     usr_in_num = int(input("please input add goods number!\n").strip())  # 输入库存商品种类数量，如上述例子就应该输入4
    # 输入商品详细情况，如商品名称，商品数量
#     input_lst = [[input("please input goods "+str(i+1)+" name and numbers!") for j in range(2)] for i in range(usr_in_num)]
#     print(input_lst)
    input_lst=[['袜子', '10'], ['鞋子', '20'], ['拖鞋', '30'], ['项链', '40']]
    lst=[]
    # 将商品存储到列表中，列表元素为商品名称
    for i in input_lst:
        for _ in range(int(i[1])):
            lst.append(i[0])
    random.shuffle(lst)  # 对列表商品打乱顺序
    return random.choice(lst)  # 随机取一个列表中的值


if __name__ == "__main__":
    type1 = 0
    type2 = 0
    type3 = 0
    type4 = 0
    num = int(input("please input test count!\n").strip())
    for i in range(num):
        result = fun_res()
        if result == "项链":
            type4 += 1
        elif result == "拖鞋":
            type3 += 1
        elif result == "鞋子":
            type2 += 1
        else:
            type1 += 1
#         print("本次随机取得的商品为："+result)
print("在{}次的测试中，商品袜子出现了{}次、鞋子出现了{}次、拖鞋出现了{}次、项链出现了{}次".format(num, type1,type2, type3, type4))
