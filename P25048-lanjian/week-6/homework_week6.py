# 1、现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
t1 = (('a'), ('b'))
t2 = (('c'), ('d'))
lst = []
for i in range(2):
    d = lambda t1, t2: {t1[i][0]: t2[i][0]}
    lst.append(d(t1, t2))
print(lst)
# 2、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
source = 'I feel no need for any other faith than my faith in human beings.'
lst = source.split()
print(lst)
lst.reverse()
print(lst)

result = ''
for i in range(len(lst)):
    result += lst[i] + " "
print('翻转之后：', result)
