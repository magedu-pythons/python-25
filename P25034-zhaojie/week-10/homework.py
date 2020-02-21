#!/usr/bin/env python
# encoding:utf-8
# file: homework.py

# 不使用系统函数，自己实现一个string类，
# 实现基本的字符串翻转reverse，索引index，大写upper，小写lower，查找find等功能


# 还没学到类，先实现一个基本的
class String(object):
    def __init__(self, s):
        self.string = s

    def __str__(self):
        return self.string

    def reverse(self):
        return self.string[::-1]

    def index(self, sub):
        for idx in range(len(self.string)):
            if sub == self.string[idx]:
                return idx
        return None

    def upper(self):
        s_tmp = ''
        for c in self.string:
            if c >= 'a' and c <= 'z':
                s_tmp += chr(ord(c) - 32)
            else:
                s_tmp += c
        return s_tmp

    def lower(self):
        s_tmp = ''
        for c in self.string:
            if c >= 'A' and c <= 'Z':
                s_tmp += chr(ord(c) + 32)
            else:
                s_tmp += c
        return s_tmp

    def find(self, substr):
        str_len = len(self.string)
        substr_len = len(substr)
        for idx in range(str_len):
            for idx2 in range(substr_len):
                # 避免字符串下标越界
                if idx + idx2 >= str_len or self.string[idx + idx2] != substr[idx2]:
                    break
            else:
                # 排除空子字符串
                if substr_len > 0:
                    return idx
        return None


if __name__ == '__main__':
    a = String('12aBa\tc')
    print(a)
    print(a.reverse())
    print(a.index('a'))
    print(a.upper())
    print(a.lower())
    print(a.find('2a'))

# 不错,写的很好,基本的功能都考虑到了，但是一些基本的异常情况没有考虑。
# 例如，如果传进去的是数字呢？
