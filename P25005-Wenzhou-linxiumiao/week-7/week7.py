a = "1,2,3"
b = a.split(',')
print(b)

f1 = 'e:/a/test1.txt'
f2 = 'e:/b/tset2.txt'

with open(f1) as line:
    with open(f2,'w') as line1:
        line1.write(line.read())

li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)

li里面的列表*5，因为做的是浅拷贝所以对其中的任意一个做append其他的列表都会做相应的改变（里面的列表指向的都是同一个）
最后一个append是单独对li进行添加对里面的列表没有影响。