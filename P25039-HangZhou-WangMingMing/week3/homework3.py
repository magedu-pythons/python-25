1.找出列表中元素是否存在，存在返回1，不存在返回0
#思路，先用for从列表中逐个取元素
#如果取出的值i=x，则打印1，然后break退出
#如果没有找到i=x，则for循环正常结束，指向else里面的打印0

for i in a:
	if i == 1:
		print(1)
		break
else:
	print(0)


2.统计英文文本中的某个单词的个数
#打开文件
#将文件内容付给字符串
#使用字符串的count功能进行统计。。。不知道对不对

a = "is"
with open("python.txt") as f:
	s = str(f.read())
	c = s.count(a)
	print(c)

