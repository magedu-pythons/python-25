#!/usr/bin/env python
# encoding:utf-8

# file: homework2.py
# author: ZhaoJie
# date: 2019/9/16

# 打印100内的斐波那契数列
# 优化代码 ref:P25020-shenzhen-liujingwei/week-2/


def fib_seq1(max_num):
    """方法1：使用循环
    """
    prev_num = 0
    next_num = 1
    while next_num < max_num:
        prev_num, next_num = next_num, prev_num + next_num
        print(prev_num, end=' ')
    print()


def pnt_fib(max_num):
    def fib_seq2(num_idx):
        """方法2：使用递归
        """
        if num_idx <= 2:
            return 1
        return fib_seq2(num_idx - 1) + fib_seq2(num_idx - 2)
    i = 1
    num = fib_seq2(i)
    while num < 100:
        print(num, end=' ')
        i += 1
        num = fib_seq2(i)
    print()


def fib_seq3(max_num):
    """方法3：使用队列
    """
    result = [0, 1]
    while result[-1] < max_num:
        result.append(result[-1] + result[-2])
    print(" ".join([str(i) for i in result[1:-1]]))


if __name__ == '__main__':
    max_fib = 100
    fib_seq1(max_fib)
    pnt_fib(max_fib)
    fib_seq3(max_fib)
