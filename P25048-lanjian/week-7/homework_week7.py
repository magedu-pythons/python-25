# 1、请将 "1,2,3"，变成 ["1","2","3"]
s = "1,2,3"
lst = s.split(',')
print(lst)

# 2、使用Python copy一个文件，从a目录,copy文件到b目录
# 还没学到文件操作

'''
3、以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
'''
# li = [ [ id()] ] * 5 li列表中含有一个空列表的引用，执行*5之后浅拷贝生成含有五个相同引用的空列表的列表=>[ [ ],[ ],[ ],[ ],[ ] ]
# li[0].append(10) 将10添加到li[0]，因为li列表中所有元素持有相同的列表引用，所以添加一个，其他列表也要添加=>[[10], [10], [10], [10], [10]]
# li[1].append(20) 原因同上，给li[1]添加元素，其他持有相同引用的列表也要添加=> [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
# li.append(30) 这只对li列表添加新的元素=> [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
# li = [[]] * 5
# for i in range(len(li)):
#     print(id(li[i]))
