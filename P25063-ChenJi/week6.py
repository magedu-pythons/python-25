#1、# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

print((lambda x, y: [{x[0]:y[0]}, {x[1]:y[1]}])((('a'),('b')),(('c'),('d'))))






#2、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
sentence = 'How are you? Fine, thank you. And you?'
words = sentence.split(" ")
words.reverse()
print(" ".join(words))

# 第一个作业完成的很好，第二个作业看一下代码里执行结果中符号的位置。题目要求单词顺序变化，你这里符号和单词一起变了。
