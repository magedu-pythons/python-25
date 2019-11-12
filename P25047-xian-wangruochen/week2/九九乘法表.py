row = 1
##嵌套循环
while row <= 9:
    col = 1
    while col <= row:
##end作用：不换行
        print("%d * %d = %d "%(col,row,col*row),end="\t")
        col += 1
##print("")的作用是另起一行
    print("")
    row += 1
















