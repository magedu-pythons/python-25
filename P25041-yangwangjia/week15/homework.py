import csv

class QuerySource():
    def __init__(self, _login_list):
        self._login_list = _login_list

    def cheek(self):
        result = self.read_file('passwd.csv')
        # print(result)
        # print("------")
        _login_type = self._login_list[0]
        _username = self._login_list[1]
        _passwd = self._login_list[2]
        # 判断用户输入的登陆用户名否存在
        _all_login_username = {_x[1] for _x in result}
        if _username not in _all_login_username:
            return "用户名不存在，请重试！"

        _count = 2  # 记录用户错误输入的次数
        for login_source in result:
            if login_source[0] == _login_type and login_source[1] == _username and login_source[2] == _passwd:
                if len(login_source) > 3:
                    if login_source[3] == "密码锁定，无法登陆!":
                        return "密码锁定，无法登陆!"
                return 200
            else:
                if login_source[1] == _username:
                    if len(login_source) > 3:
                        if login_source[3] == "密码锁定，无法登陆!":
                            return "密码锁定，无法登陆!"
                    elif login_source[0] != _login_type:
                        return "账户类型不匹配，请重试！"
                    else:
                        pass
                    while _count:
                        _count -= 1
                        usr_passwd_again = input("Password error, try again !\n")
                        # print(_passwd,login_source[2])
                        if login_source[2] == usr_passwd_again:
                            return 200
                    self.writr_file('passwd.csv', self._login_list, lock=True, mode='w', username=_username, line=False)  # 锁定账号
                    return "密码锁定，无法登陆!", "密码尝试失败次数过多！！！"

    def writr_file(self, filename, src, lock=False, mode='a', username=None, line=True):
        # 锁定账户
        if lock:
            _results = self.read_file(filename)
            for _login_source in _results:
                if _login_source[1] == username:
                    # print("!!!锁定用户{}账号!!!".format(username))
                    _login_source.append("密码锁定，无法登陆!")
            src = _results
        with open(filename, mode=mode, newline='') as f_write:
            csvfile_write = csv.writer(f_write)
            if line:
                csvfile_write.writerow(src)
            else:
                csvfile_write.writerows(src)

    def read_file(self, filename):
        with open(filename, 'r', newline='') as f_read:
            csvfile_read = csv.reader(f_read)
            return list(csvfile_read)

    def source(self):

        def _query_again():  # 继续查询函数
            _continue = input("是否继续查询？>>\n")
            if _continue in {'NO', 'QUIT', 'Q', 'N', 'quit', 'n', 'q', 'no', '否', '退出', '不是'}:  # 不继续查询
                return 0
        while True:
            filename = 'score.csv'
            _ret = self.read_file(filename)

            query_name = input("请输入要查询的学生名称！>>\n")
            for cource in _ret:
                if cource[0] == query_name:
                    return query_name, cource[1], cource[2], cource[3]
            if self._login_list[0] == "教师":  # 登陆类型为教师
                _continue = input("查询学生不存在，是否输入该学生成绩？>>\n")
                if _continue in {'是', 'yes', 'YES', 'Y', 'y'}:  # 输入成绩步骤
                    while True:
                        teacher_input = input("请依次输入{}的语文、数学、英语成绩，中间以英文逗号分隔！\n".format(query_name))
                        src = teacher_input.split(',')
                        if len(src) == 3:
                            break
                        print("成绩信息输入有误，请重新输入！\n")
                    src.insert(0, query_name)
                    self.writr_file(filename, src)
                    print("输入{}信息成功".format(query_name))
                else:  # 询问是否继续查询
                    if _query_again() == 0:
                        return 0
            else:  # 登陆类型为学生,询问是否继续查询
                print("查询学生不存在！")
                if _query_again() == 0:
                    return 0
                print('========')



class App():
    """ 系统简介：

    系统默认用户
    登录类型   用户名       密码
    教师       teacher     123456
    学生       student     123456

    系统默认成绩
    学生姓名   语文成绩    数学成绩     英语成绩
    test1      100         99          100
    test2      98          100         100

    当程序运行时，询问用什么角色登陆。角色有老师和学生。
    然后输入用户名和密码验证，验证错误三次，提示密码锁定，无法登陆，但是可以用其他用户登录。
    然后询问需要查询的名称，如果可以查到该用户，返回该用户的语文、数学、英语的成绩。
    如果没有，学生角色提示是否查询下一个，不查询就退出。

    如果是教师角色，则提示是否输入该用户成绩，
    是，则进入输入成绩步骤，输入完成后，将成绩保存到文件中。
    否，则询问是否继续查询。如果继续查询，则进入查询步骤，如果不查询，则退出
    """
    def run(self):
        print("====================================\n|welcome to query report programer!|\n====================================\n")
        while True:
            print("\n\n========\n|1.教师|\n|2.学生|\n========")
            type_dict = {1: '教师', 2: '学生'}
            # 判断用户输入角色是否合法
            while True:
                try:
                    usr_type = int(input("who are you ? please select number !>>\n").strip())
                except Exception as e:
                    print("Input TypeError, please try again !\n")
                else:
                    if usr_type in type_dict:
                        break
                    else:
                        print("Input ValueError, please try again !\n")

            # 进入登录验证
            usr_username = input("please input login name!>>\n")
            usr_password = input("please input password!>>\n")
            query = QuerySource([type_dict[usr_type], usr_username, usr_password])
            ret = query.cheek()
            if ret == 200:
                print("登陆成功！\n")
                query_source_ret = query.source()
                if query_source_ret == 0:
                    print('bye~~~')
                    break
                else:
                    print("======="*3)
                    print("学生{}的成绩如下：\n语文：{}分\n数学：{}分\n英语：{}分".format(*query_source_ret))
                    print("=======" * 3)
                    usr_quit = input("是否退出？(输入q退出)\n")
                    if usr_quit == 'q':
                        print('bye~~~')
                        break
            else:
                print(ret)

    def init_src(self):
        """ 这是初始化文件，该文件用来恢复数据

        :return:
        """
        def _init_passwd():
            """ 登陆账号初始化

            初始化用户登陆账号密码函数
            :return:
            """
            src = [['教师', 'teacher', '123456'], ['学生', 'student', '123456']]
            with open('passwd.csv', mode='w', newline='') as f_write:
                csvfile_write = csv.writer(f_write)
                csvfile_write.writerows(src)

        def _init_source():
            """ 成绩初始化

            初始化成绩函数
            :return:
            """
            src = [['test1', '100', '99', '100'], ['test2', '98', '100', '100']]
            with open('score.csv', mode='w', newline='') as f_write:
                csvfile_write = csv.writer(f_write)
                csvfile_write.writerows(src)

        _init_passwd()  # 初始化用户登录文件
        _init_source()  # 初始化成绩文件

if __name__ == "__main__":
    """ 系统简介：
    
    系统默认用户
    登录类型   用户名       密码
    教师       teacher     123456
    学生       student     123456
    
    系统默认成绩
    学生姓名   语文成绩    数学成绩     英语成绩
    test1      100         99          100
    test2      98          100         100
    
    """
    app = App()
    print(app.__doc__)  # 帮助文档
    # app.init_src()初始化数据程序,正常运行时用不到。
    # 执行init_src()会将成绩文件和登陆帐号文件恢复到初始值,请慎用
    # app.init_src()
    app.run()
