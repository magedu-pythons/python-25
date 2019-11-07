# 使用两元组(('a'),('b')),(('c'),('d')),请使用Python中的匿名函数生成列表[{'a':'c'},{'b':'d'}]
"""
先留空，学到匿名函数后再来写此题
"""




# 输入一个英文句子，翻转句子中的单词顺序，但单词内字符的顺序不变
usr_in = 'Whatever is worth doing is worth doing well.'

tmp = usr_in.strip().rstrip(' .?!')
# print(tmp)
lst = tmp.split(' ')
res = lst[::-1]
res = ' '.join(map(str,res))
print(res)
