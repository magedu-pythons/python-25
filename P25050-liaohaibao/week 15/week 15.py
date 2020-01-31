# 本周作业：写一个查询成绩程序，程序中定义一个类，类里面有验证函数，写文件函数和读文件函数。当程序运行时，
# 询问用什么角色登陆。然后输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
# 角色有老师和学生。然后询问需要查询的名称，如果可以查到该用户，返回该用户的语文、数学、英语的成绩。如果没有，
# 学生角色提示是否查询下一个，不查询就退出。
# 如果是教师角色，则提示是否输入该用户成绩，是，则进入输入成绩步骤，输入完成后，将成绩保存到文件中。
# 否，则询问是否继续查询。如果继续查询，则进入查询步骤，如果不查询，则退出。
import os

class ScoreManage:
    #初始化类实例
    def __init__(self):
        isteacher = input("您是老师吗？Y/N>>>")   # 询问用什么角色登陆
        if isteacher == 'Y':
            self.role = 'teacher'
        else:
            self.role = 'student'

        self.score = {}  # 保存学生成绩，格式‘姓名’：‘语文100、数学100、英语100’
        self.userinfo = {'teacher':{'t1':'123','t2':'123'},'student':{'s1':'123','s2':'123'}} #初始化老师、学生的帐号和密码
        self.loginerror = {} # 错误登陆用户次数
        self.userlogin() # 调用登陆方法

    # 输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
    def userlogin(self):
        login = False  #输入帐号和密码正确为True
        while True:
            self.username = input("输入登陆名：>>>")
            if self.userinfo[self.role].get(self.username, False):  # 判断用户是否存在
                self.password = input("输入密码：>>>")
            else:
                print('输入的登陆帐号有不存在！')
                continue

            if self.loginerror.get(self.username,False): # 验证错误三次，提示密码锁定
                    if self.loginerror[self.username] >= 3:
                        print('帐号{}密码输入错误次数达到3次，该帐号已锁定'.format(self.username))
                        otheruser = input("是否用他帐号登陆？Y/N：>>>") #提示是否换帐号登陆
                        if otheruser == 'Y':
                            continue
                        else:
                            break

            if self.password != self.userinfo[self.role][self.username]:
                self.loginerror[self.username] = self.loginerror.get(self.username,0) + 1
                print('登陆密码有误，请重新输入！注：错误达到3次帐号将锁定')
            else:
                login = True
                break


        if login == False:
            return

        self.readscore() #成功登陆后，进入学生成绩查询方法

    # 读取学生成绩
    def readscore(self):
        if not os.path.exists('d:/abc.txt'): #判断成绩单是否存在，不存在就创一个建空文件
            open('d:/abc.txt','w+',encoding='utf-8')

        with open('d:/abc.txt', encoding='utf-8') as lines:
            for line in lines: #读取出文件中的成绩，写入字典中
                self.score[line.split(":")[0]] = line.split(":")[1] #{‘学生名’：‘各科成绩’}

            while True:
                name = input("输入学生姓名：>>>")
                if self.score.get(name,False):
                    print('{}成绩是：{}'.format(name,self.score[name])) #打印成绩单
                    break
                else:
                    if self.role == 'teacher':
                        if input("该学生成绩不存在，是否输入该学生成绩? Y/N:>>>") == 'Y':
                            self.writescore(name)

                        if input("是否继续查询? Y/N:>>>") == "Y":
                            continue
                        else:
                            break
                    else:
                        if input("该学生成绩不存在，是否查询下一个? Y/N: >>>") == "Y":
                            continue
                        else:
                            break

    # 写入学生成绩
    def writescore(self,name:str):
        with open('d:/abc.txt', 'w+', encoding='utf-8') as f:
            scorevalue = '语文{}'.format(input("语文成绩 >>>"))
            scorevalue += '、数学{}'.format(input("数学成绩 >>>"))
            scorevalue += '、英语{}'.format(input("英语成绩 >>>"))
            f.writelines(['{}:'.format(name),scorevalue])
            self.score[name] = scorevalue
            print('成绩已保存！')


if __name__ == '__main__':
    ScoreManage()

