# encoding:utf8

"""
2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数
"""

# 上述问题即求加权随机数
import random


def pick(goods_d, rnd_num):
    """
    商品选取函数
    :param goods_d: 商品字典
    :param rnd_num: 随机数
    :return: 商品名称
    """
    pos = 0
    for item in goods_d:
        if rnd_num > pos and rnd_num <= pos + goods_d[item]:
            return item
        pos += goods_d[item]


if __name__ == '__main__':
    # 定义商品字典
    goods_dict = {
        'socks': 10,  # 袜子
        'shoes': 20,  # 鞋子
        'slipper': 30,  # 拖鞋
        'necklace': 40  # 项链
    }
    # 计算总权重
    total_w = sum(goods_dict.values())
    # 返回商品名
    tmp_num = random.randint(1, total_w)
    print(tmp_num, pick(goods_dict, tmp_num))
