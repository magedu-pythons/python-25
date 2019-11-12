# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
t1 = (('a'),('b'))
t2 = (('c'),('d'))
f = lambda t1,t2:[{t1[i]:t2[i]} for i in range(len(t1))]
print(f(t1,t2))

# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
s = 'which one do you like best'
ret = ' '.join(s.split()[::-1])
print(ret)