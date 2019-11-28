# 1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
def find_str(src, sub):
    # s = str(src)
    index = src.find(sub)
    if index > 0:
        return index
    else:
        return None


result = find_str('I like python', 'like')
print(result)

'''
2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
'''
lst = list(range(1, 100))


def find_nums(x):
    # 方法1使用嵌套循环
    # result = []
    # for i in range(len(lst)):
    #     for j in range(i + 1, len(lst)):
    #         if i + j == x:
    #             result.append((i, j))
    # return result
    # 方法2使用列表解析式
    return [(i, j) for i in range(len(lst)) for j in range(i + 1, len(lst)) if i + j == x]


s = find_nums(15)
print(s)
