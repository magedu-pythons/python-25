# 本周作业：写一个查询成绩程序，程序中定义一个类，类里面有验证函数，写文件函数和读文件函数。当程序运行时，
# 询问用什么角色登陆。然后输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
# 角色有老师和学生。然后询问需要查询的名称，如果可以查到该用户，返回该用户的语文、数学、英语的成绩。如果没有，
# 学生角色提示是否查询下一个，不查询就退出。
# 如果是教师角色，则提示是否输入该用户成绩，是，则进入输入成绩步骤，输入完成后，将成绩保存到文件中。
# 否，则询问是否继续查询。如果继续查询，则进入查询步骤，如果不查询，则退出。
import pymysql
import os

class ScoreManage:
    #初始化类实例
    def __init__(self):
        self.loginerror = {} # 错误登陆用户次数
        self.group = 2 #默认角色为学生

    #连接数据库
    def __enter__(self):
        self.conn = pymysql.connect('127.0.0.1', 'root', 'root', 'score_db')
        self.cursor = self.conn.cursor()
        self.userlogin()

    # 执行sql语句,默认为查询
    def execute_sql(self,sql,type = 0):
        if type == 0:
            return self.cursor.execute(sql)
        else:
            try:
                rows = self.cursor.execute(sql)
                self.conn.commit()
            except:
                self.conn.rollback()
            return rows

    #退出时结束连接符
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # 输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
    def userlogin(self):
        login = False  #输入帐号和密码正确为True
        while True:
            username = input("输入登陆名：>>>")
            password = input("输入密码：>>>")
            sql = "select id,name,groupId,password from user where name = '{0}'".format(username)
            if self.execute_sql(sql): # 判断用户是否存在
                row = self.cursor.fetchall()[0]
                self.group = row[2]
                while True:
                    if password != row[3]:
                        self.loginerror[username] = self.loginerror.get(username, 0) + 1
                        if self.loginerror[username] >= 3: # 验证错误三次，提示密码锁定
                            print('帐号{}密码输入错误次数达到3次，该帐号已锁定'.format(username))

                            if input("是否用他帐号登陆？Y/N：>>>") == 'Y': #提示是否换帐号登陆
                                break
                            else:
                                return
                        else:
                            print('登陆密码有误，请重新输入！注：错误达到3次帐号将锁定')
                            password = input("输入密码：>>>")
                    else:
                        login = True
                        break
                if login:
                    break;
            else:
                print('输入的登陆帐号有不存在！')
                continue

        if login == False:
            return

        self.readscore() #成功登陆后，进入学生成绩查询方法

    # 读取学生成绩
    def readscore(self):
        while True:
            username = input("输入学生姓名：>>>")
            sql = "select id,name,groupId,password from user where name = '{0}'".format(username)
            if self.execute_sql(sql):  # 判断学生是否存在
                userrow = self.cursor.fetchall()[0]
            else:
                continue

            sql = "select score from score where userId = '{0}'".format(userrow[0])
            if self.execute_sql(sql):  # 成绩是否存在
                scorerow = self.cursor.fetchall()[0]
                print('{}成绩是：{}'.format(username,scorerow[0])) #打印成绩单
                break
            else:
                if self.group == 1:
                    if input("该学生成绩不存在，是否输入该学生成绩? Y/N:>>>") == 'Y':
                        self.writescore(userrow[0])

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
    def writescore(self,userId:int):
        scorevalue = '语文{}'.format(input("语文成绩 >>>"))
        scorevalue += '、数学{}'.format(input("数学成绩 >>>"))
        scorevalue += '、英语{}'.format(input("英语成绩 >>>"))

        sql = "insert into score(userId,score) values({0},'{1}')".format(userId,scorevalue)
        if self.execute_sql(sql,1):
            print('成绩已保存！')


if __name__ == '__main__':
    with ScoreManage() as sm:
        pass

