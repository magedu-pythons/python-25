# 查询成绩程序，# 程序中定义一个类，类里面有验证函数，写文件函数和读文件函数。
# 当程序运行时，询问用什么角色登陆。然后输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
# 角色有老师和学生。
# 然后询问需要查询的名称，如果可以查到该用户，返回该用户的语文、数学、英语的成绩。
# 如果没有，学生角色提示是否查询下一个，不查询就退出。
# 如果是教师角色，则提示是否输入该用户成绩，
# 是，则进入输入成绩步骤，输入完成后，将成绩保存到文件中。
# 否，则询问是否继续查询。如果继续查询，则进入查询步骤，
# 如果不查询，则退出。

import csv

USER_FILE = 'F:/Grade/user.csv'
GRADE_FILE = 'F:/Grade/grade.csv'

class Grade:
    def __init__(self,userfile,gradefile):
        self.role = ''
        self.username = ''
        self.userfile = userfile   #用户名密码角色
        self.gradefile = gradefile #成绩
        self.userdeny = []

    def auth(self):
        WrongTime = 1
        username = input('Username:')
        if username in self.userdeny:
            print('该用户已被禁用,请使用其他用户登录！')
            return False
        with open(self.userfile) as f:
            reader = csv.reader(f)
            while True:
                password = input('Password:')
                for line in reader:
                    if tuple(line)==(self.role,username,password):
                        self.username = username
                        return True
                else:
                    WrongTime += 1
                    if WrongTime>3:
                        self.userdeny.append(username)
                        print('用户{}已被锁定'.format(username))
                        return False
                    else:
                        continue

    def write_score(self,stu):
        ch = input('{} ch Grade:'.format(stu))
        ma = input('{} math Grade:'.format(stu))
        en = input('{} en Grade:'.format(stu))
        Grade = [stu,ch,ma,en]
        with open(self.gradefile, 'a+', encoding='utf-8') as f:
            csv.writer(f).writerow(Grade)

    def read_score(self,stu):
        with open(self.gradefile) as f:
            reader = csv.reader(f)
            for line in reader:
                if stu in line:
                    return tuple(line)
            else:
                return ()

    def modify_grade(self):
        while True:
            stu = input('Input StudentName(q for quit):')
            if stu=='q':break
            if stu=='':continue
            ret = self.read_score(stu)
            if ret:
                print(ret)
            else:
                add = input('add {} Grade?(y/n)'.format(stu))
                if add =='y':
                    if self.role=='t':
                        self.write_score(stu)
                    if self.role=='s':
                        print("Stu Can't Input Grade.")
                else:
                    continue

    def run(self):
        while True:
            role = input('Plz Input Your Role(s/t)(q for quit):').strip().lower()
            if role=='q':break
            if role=='':continue
            if role=='s' or role== 't':
                self.role=role.strip().lower()
                login = self.auth()
                if  not login:
                    continue
                else:
                    print('{}:{}登录成功'.format(self.role,self.username))
                    self.modify_grade()

g = Grade(USER_FILE,GRADE_FILE)
g.run()
#g.auth()

# 功能实现的很好，就是后面测试的时候，尽量把你的数据文件也传上来，这样更方便测试
