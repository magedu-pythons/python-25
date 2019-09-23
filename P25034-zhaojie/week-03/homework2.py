#!/usr/bin/env python
# encoding:utf-8
# file: homework2.py

# 统计英文单词数


def wc(fn):
    """以空格分隔的连续字符串为单词
    """
    with open(fn, 'r') as fd:
        words = fd.read().split()
        print(len(words))


wc('sample.txt')
wc('sample2.txt')
