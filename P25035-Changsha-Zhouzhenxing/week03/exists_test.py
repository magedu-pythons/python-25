# 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0 
def exists(x, list):
    if x in list:
        return 1
    else:
        return 0

if __name__ == '__main__':
    list = ['A', 'B', 'C']
    print(exists('F', list))
