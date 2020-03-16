"""
本周作业：
写一个查询成绩程序，程序中定义一个类，类里面有验证函数，写文件函数和读文件函数。
当程序运行时，询问用什么角色登陆。然后输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
角色有老师和学生。然后询问需要查询的名称，如果可以查到该用户，返回该用户的语文、数学、英语的成绩。
如果没有，学生角色提示是否查询下一个，不查询就退出。
如果是教师角色，则提示是否输入该用户成绩，是，则进入输入成绩步骤，输入完成后，将成绩保存到文件中。
否，则询问是否继续查询。如果继续查询，则进入查询步骤，如果不查询，则退出。
"""

import json

ACCOUNT_PATH = 'account.txt'
FILE_PATH = 'user.txt'
ACCOUNT = {'test': '123456', 'jack': '111111', 'sam': '000000'}


class Student:
    def __init__(self, name: str, chinese: str, math: str, english: str):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return "'name':{},'chinese':{},'math':{},'english':{}".format(self.name, self.chinese, self.math, self.english)


def hook(d):
    return Student(d['name'], d['chinese'], d['math'], d['english'])


class UserManager:

    def __init__(self):
        self.lock_user = []  # 被锁住的用户

    def work(self):
        i = int(input('请选择登陆角色：\n\t1-老师 \n\t2-学生\n\t'))
        print(i)
        self.login(i)

    # 登录
    def login(self, user_type, count=3):
        # 校验账户
        name = ''
        pwd = ''

        while name == '':
            name = input('请输入用户名：').strip().lower()
            print(name)
            if name == '':
                print('账号不能为空！')

            if name in self.lock_user:
                print('该账号被锁，请使用其他账户登陆！')
                self.login(user_type)
                return

            if name not in ACCOUNT.keys():
                print('该账号不存在')
                name = ''

        while count > 0:
            pwd = input('请输入密码：').strip().lower()
            print(pwd)
            if pwd == '':
                print('密码不能为空！')

            if pwd == ACCOUNT[name]:
                break
            else:
                count = count - 1
                if count == 0:
                    print('密码输入次数超过3次，账号被锁定！')
                    self.lock_user.append(name)
                    self.login(user_type)
                    return

        # 查询用户信息
        self.query(user_type)

    # 查询用户信息
    def query(self, user_type):
        name = input('请输入需要查询的名称：')
        student = self.readfile(name)
        # print('查询：', student)
        if student is None:  # 查询不到
            if user_type == 1:  # 如果是老师，提示是否录入该学生信息
                i = input('是否输入该用户成绩:y/n?')
                if i == 'y':
                    chinese = input('请输入语文成绩：')
                    math = input('请输入数学成绩：')
                    english = input('请输入英语成绩：')
                    student = Student(name, chinese, math, english)

                    self.writefile(student)  # 保存该学生信息
                else:
                    i = input('是否继续查询:y/n?')
                    if i == 'y':  # 继续查询
                        self.query(user_type)
                    else:  # 不查询，退出系统
                        print('退出系统')

            else:  # 如果是学生登陆，提示是否查询下一个
                i = input('查询不到该用户，是否查询下一个:y/n?')
                if i == 'y':  # 继续查询下一个
                    self.query(user_type)
                else:  # 不查询，退出系统
                    print('退出系统')

        else:
            print('查询结果：', student)

    # 写文件，将该用户的成绩写入文件
    @staticmethod
    def writefile(student: Student):
        info = student.__dict__
        print('write student:', info)
        result = json.dumps(info)  # 序列化student
        # print('dump json:', result)
        with open(FILE_PATH, mode='a') as f:
            f.write(result + "\n")

    # 读文件,查询该用户的成绩
    @staticmethod
    def readfile(name: str):
        with open(FILE_PATH) as f:
            result = None
            for l in f.readlines():
                # print('read lines:',l)
                student = json.loads(l, object_hook=hook)  # 反序列化student
                # print('load json:', student.__dict__)
                if student.name == name:
                    result = student
            # print('查询到该用户：',result.__dict__)
            return result


# 测试数据
# s =Student(name='tom',chinese='70',math='80',english='60')
# UserManager.writefile(s)
# s =Student(name='jerry',chinese='80',math='70',english='90')
# UserManager.writefile(s)
# s =Student(name='lina',chinese='90',math='80',english='70')
# UserManager.writefile(s)
# s =Student(name='lily',chinese='60',math='90',english='80')
# UserManager.writefile(s)

# UserManager.readfile('tom')
# UserManager.readfile('jerry')


manager = UserManager()
manager.work()
