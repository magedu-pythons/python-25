# 请将 "1,2,3"，变成 ["1","2","3"]
usr_in = "1,2,3"
res = usr_in.split(",")
print(res)



# 使用Python copy一个文件，从a目录,copy文件到b目录
def my_copy(filename,oldpath,newpath):
    try:
        f = open(oldpath+filename,'rb')
        tmp = f.read()
    finally:
        f.close()
        
    try:
        f2 = open(newpath+filename,'wb')
        f2.write(tmp)
    finally:
        f2.close()
    return '程序运行结束'

if __name__ == "__main__":
    # 程序运行前置条件当前目录下存在a.txt，且存在上一级目录
    my_copy('a.txt','./','../')
