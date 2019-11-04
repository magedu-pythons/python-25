#!/usr/bin/env python
# encoding:utf-8
# file: homework2.py

# 输入一个英文句子，翻转句子中的单词顺序，但单词内字符的顺序不变
# 例句："My name is Bob, and What's your name? Oh, Eve. "
# 结果：" Eve. Oh, name? your What's and Bob, is name My"


# 用内置函数split
def reverse_sentence():
    sentence = input('Please type a sentence: ')
    word_lst = sentence.split()
    # 句子两侧空格会丢失
    # 单词之间多个空格会变成一个
    print(' '.join(word_lst[::-1]))


# 从尾部遍历句子
def reverse_sentence2():
    sentence = input('Please type a sentence: ')
    # 单词分隔符
    word_sep = ' '
    position = len(sentence) - 1
    while position >= 0:
        tmp_stack = []
        while position >= 0 and sentence[position] != word_sep:
            tmp_stack.append(sentence[position])
            position -= 1
        print(''.join(tmp_stack[::-1]), end='')
        # 只在是空格的情况打印空格
        if position >= 0:
            print(word_sep, end='')
        position -= 1


reverse_sentence()
reverse_sentence2()
