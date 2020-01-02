1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
def found_child_str(str1: str,str2: str)->str:
    index = str1.find(str2)
    if index != -1:
        return index
    else:
        return None

if __name__ == "__main__":
    print(found_child_str('1245453','453'))
















2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？

如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
def found_num(lst: list, target: int)->str:
    flag = False
    for i in lst:
        tmp = target - i
        if tmp in lst:
            flag = True
            break
    if flag:
        return i,tmp
    else:
        return 'Not Found!'

    
if __name__ == "__main__":
    print(found_num([1,5,2,7,4,9],11))
    print(found_num([1,5,2,7,4,9],16))
    print(found_num([1,5,2,7,4,9],1))
