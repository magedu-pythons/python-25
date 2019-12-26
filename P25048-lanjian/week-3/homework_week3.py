# 1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
lst = list(range(1, 100))
print('已知列表：', lst)
val = int(input('输入要查找的数字:'))
result = 0
for i in lst:
    if val == i:
        result = i
        break
if result:
    print('找到您的数字 ', val, ',它的位置在', lst.index(result))
else:
    print('很遗憾没找到您的数字 ', val)

# 2、任一个英文的纯文本文件，统计其中的单词出现的个数
source = '''
I believe in human beings, but my faith is without sentimentality. 
I know that in environments of uncertainty, fear, and hunger, 
the human being is dwarfed and shaped without his being aware of it, 
just as the plant struggling under a stone does not know its own condition. 
Only when the stone is removed can it spring up freely into the light. 
But the power to spring up is inherent, and only death puts an end to it.
I feel no need for any other faith than my faith in human beings.
'''
source = source.replace(',', ' ')
# print('去掉逗号之后：', source)
source = source.replace('.', ' ')
# print('去掉句号之后：', source)
lst = source.split()
print('分割成一个个单词:', len(lst), '个 ', lst)
s = set(lst)
# print('添加到集合去重之后：', len(s), '个 ', s)
dic = dict.fromkeys(lst, 0)  # 用键值对保存统计的值，key-被统计的单词，value-单词个数
print('转换成字典去重之后：', len(dic), '个', dic)
for key in s:
    for i in lst:
        if i == key:
            dic[key] += 1

print('统计结果：', dic)
