str2 = 'lxm'
str1 = 'adfafeldsalxqwelxmgwrlxmwqeq'

def strjudgement(str1:str,str2:str):
    if str2 in str1:
        return len((str1.split(str2))[0])
    else:
        return None

print(strjudgement(str1, str2))


lst = [1,5,2,7,4,9]
num = 11

def fund_add(lst:list, n:int):
    lens = len(lst)
    for x in range(lens):
        for y in range(x,lens):
            if lst[x] + lst[y] == n:
                return '{} + {} = {}'.format(lst[x], lst[y], n)
    else:
        return 'Defund two numbers add for{}'.format(n)

print(fund_add(lst, num))


def fund_add(lst:list, n:int):
    d = {}
    for i,v in enumerate(lst):
        if d.get(n-v) is not None:
            return '{} + {} = {}'.format(v,n-v,n)
        d[v] = i




print(fund_add(lst, num))