# 不使用系统函数，自己实现一个string类，实现基本的字符串翻转reverse，索引 index，大写upper，小写lower，查找find等功能
class String(str):
    def reverse(self):
        lst = list(self)   #使用list的翻转函数
        lst.reverse()
        return ''.join(lst)
    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count
    def __getitem__(self, index):
        return list(self)[index]
    def up(self):
        tmp = ''
        for ch in self:
            if ord(ch) >= 97 and ord(ch) <= 122:
                tmp += chr(ord(ch)-32)
            else:
                tmp += ch
        return tmp
    def lw(self):
        tmp = ''
        for ch in self:
            if ord(ch) >= 65 and ord(ch) <= 90:
                tmp += chr(ord(ch)+32)
            else:
                tmp += ch
        return tmp
    def findS(self,ch):
        for i in range(len(self)):
            if self[i] == ch:
                return i
        else:
            return -1

s = String('hello world!12')
print(s.reverse())
print(s[2])
print(s.up())
print(s.lw())
print(s.findS('d'))
