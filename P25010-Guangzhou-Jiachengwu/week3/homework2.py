# 任一个英文的纯文本文件，统计其中的单词出现的个数
import os
Doc_file=os.popen('cat maclist').read()

Words=Doc_file.splitlines()

Dic_Words={}

for word in Words:
    if word not in Dic_Words:
        Dic_Words[word]=1
    else:
        Dic_Words[word]+=1

for k,v in Dic_Words.items():
    print("{} ==> {}次".format(k,v))