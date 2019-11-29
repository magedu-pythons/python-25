#不使用系统函数，自己实现一个string类，
# 实现基本的字符串翻转reverse，索引 index，大写upper，小写lower，查找find等功能

class strhandle:

    def __init__(self,str:str):
        self._str = str
        self._strlen = len(str)

    def _reverse(self):
        '''
        str reverse
        :return: str
        '''
        newstr = ''
        for i in range(self._strlen-1,-1,-1):
            newstr += self._str[i]
        return newstr

    def _index(self,i:int=None):
        if i==None:
            print('Plz Input Index num')
            index = int(input('>>>'))
        else:
            index = i

        if index > self._strlen:
            print('Out of Index')
            return None
        elif index < 0:
            print('Out of Index')
            return None
        else:
            return self._str[index]

    def _upper(self):
        return self._str.upper()

    def _lower(self):
        return self._str.lower()

    def _search(self,target:str=None):
        if target==None:
            print('error')
            return False
        lentarget = len(target)
        ret = []
        if lentarget > self._strlen:
            print('error')
        else:
            for i in range(self._strlen-lentarget+1):
                if self._str[i:i+lentarget] == target:
                    ret.append(i)
        if ret:
            return target,ret
        else:
            return target,0


str = '289f8349 abc0ftFWE$uab c209abc'
c = strhandle(str)
print(c._reverse())
print(c._index(-1))
print(c._index(3))
print(c._upper())
print(c._lower())
print(c._search())
print(c._search('abc'))
print(c._search('abccc'))