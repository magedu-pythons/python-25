#!/usr/bin/env python
# encoding:utf-8

# file: homework3.py
# author: ZhaoJie
# date: 2019/9/16

# 随机生成200无重复激活码，字符串长度大于5以上

import random
import string

tmp_str = string.ascii_letters + string.digits
rnd_count = 200

# 使用 random.choices
for i in range(rnd_count):
    new_str = ''.join(random.choices(tmp_str, k=8))
    print(new_str)

# 使用 random.sample
print('--------')
for j in range(rnd_count):
    new_str = ''.join(random.sample(tmp_str, k=8))
    print(new_str)
