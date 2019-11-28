# 给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

def add_list(li:list,liadd:int):
    rult=[]
    for i in li:
        s=liadd-i
        if s==i and li.count(i) >=2:
            rult.append((i, s))
            continue

        if s in li:
            rult.append((i,s))
    return rult

lst =[5,2,7,4,2,45,5,5,9,9]
print(add_list(lst,11))


