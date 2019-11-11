#1、请将 "1,2,3"，变成 ["1","2","3"]
s = "1,2,3"
s = s.split(',')
print(s)

#2、使用Python copy一个文件，从a目录,copy文件到b目录
from pathlib import Path
import shutil
p = Path()
Path('a').mkdir(exist_ok=True)
Path('b').mkdir(exist_ok=True)
a = p /'a'/'test.txt'
b = p /'b'/'test.txt'
a.write_text('you are a boy')
shutil.copy(str(a),str(b))

# 3、以下代码输出什么，请解释原因(写到问题下方):
# li = [ [ ] ] * 5
# li[0].append(10)
# print(li)
# li[1].append(20)
# print(li)
# li.append(30)
# print(li)

# 输出：
# [[10],[10],[10],[10],[10]]
# [[10,20],[10,20],[10,20],[10,20],[10,20]]
# [[10,20],[10,20],[10,20],[10,20],[10,20],30]
#
# 原因：[[]]*5是5个空列表引用的复制，复制的是列表的地址，浅拷贝，只要有一个有变动，5个列表同样变化