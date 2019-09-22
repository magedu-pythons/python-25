#!/usr/bin/env python
# encoding:utf-8

# file: homework2.py
# author: ZhaoJie
# date: 2019/9/16

# 打印100内的斐波那契数列


def fib_seq1(max_num):
    """方法1：使用循环
    """
    prev_num = 0
    next_num = 1
    print(next_num, end=' ')
    while True:
        curr_num = prev_num + next_num
        if curr_num < max_num:
            print(curr_num, end=' ')
            prev_num = next_num
            next_num = curr_num
        else:
            print()
            break


def pnt_fib(max_num):
    def fib_seq2(num_idx):
        """方法2：使用递归
        """
        if num_idx <= 2:
            return 1
        result = fib_seq2(num_idx - 1) + fib_seq2(num_idx - 2)
        return result
    for i in range(1, 100):
        curr_num = fib_seq2(i)
        if curr_num < max_num:
            print(curr_num, end=' ')
        else:
            print()
            break


def fib_seq3(max_num):
    """方法3：使用队列
    """
    result = [0, 1]
    while True:
        if result[-1] < max_num:
            result.append(result[-1] + result[-2])
        else:
            print(result[1:-1])
            break


if __name__ == '__main__':
    max_fib = 100
    fib_seq1(max_fib)
    pnt_fib(max_fib)
    fib_seq3(max_fib)
