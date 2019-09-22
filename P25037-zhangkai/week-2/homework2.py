#2、打印出100以内的斐波那契数列，使用2种方法实现

#以下脚本已通过jupter环境测试验证

#1 使用while循环
s1 = 1
s2 = 1
print(s1)
print(s2)
while True:
    s3 = s1 + s2
    if s3 > 100:
        break
    print(s3)
    s1 = s2
    s2 = s3

#2 
