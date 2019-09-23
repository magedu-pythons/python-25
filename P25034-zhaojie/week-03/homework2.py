#!/usr/bin/env python
# encoding:utf-8
# file: homework2.py

# 统计英文单词数


def wc(fn):
    """方法1：以空格分隔的连续字符串为单词
    """
    with open(fn, 'r') as fd:
        words = fd.read().split()
        print(len(words))


def wc2(fn):
    """方法2：定义单词函数遍历所有字符
    """
    word_count = 0
    word_flag = 0
    with open(fn, 'r') as fd:
        chars = fd.read()
        for i in chars:
            if i not in (' ', '\t', '\n') and word_flag == 0:
                word_count += 1
                word_flag = 1
            elif i in (' ', '\t', '\n'):
                word_flag = 0
        print(word_count)


wc('sample.txt')
wc('sample2.txt')

wc2('sample.txt')
wc2('sample2.txt')

wc('sample3.txt')
wc2('sample3.txt')
