import random
def acodes(length,n):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    res = set()
    while len(res) != n:       #循环生成n个激活码
        acode = ''
        for _ in range(length):      #生成length长度的激活码
            index = random.randint(0,61)     #随机生成s的index
            acode += s[index]
        res.add(acode)
    return res

length = int(input('请输入激活码长度：'))
res = acodes(length,200)
print(res)
