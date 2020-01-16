class Query:
    def __init__(self):
        self.teacher_dict = {'jerry':['123',0],'tom':['456',0]}
        self.student_dict = {'jim':['135',0],'faker':['777',0]}
        self.teacher_flag = False
        self.student_flag = False
        self.input_name = ''
        self.achievement = {}

    def sign_in(self):
        choice = input('Teacher input 1 , Other is student:')
        if choice == '1':
            d = self.teacher_dict
            while True:
                name = input('Account:')
                if name in d:
                    while d[name][1] < 3:
                        password = input('password:')
                        if password == d[name][0]:
                            print('Welcome {}'.format(name))
                            self.teacher_flag = True
                            d[name][1] = 0
                            self.query()
                            self.sign_in()
                        else:
                            d[name][1] += 1
                    else:
                        print('Password locked, unable to log in')
                else:
                    print('No User')
        else:
            d = self.student_dict
            while True:
                name = input('Account:')
                n = 0
                if name in d:
                    while d[name][1] < 3:
                        password = input('password:')
                        if password ==d[name][0]:
                            print('Welcome {}'.format(name))
                            self.student_flag = True
                            d[name][1] = 0
                            self.query()
                            self.sign_in()
                        else:
                            d[name][1] += 1
                    else:
                        print('Password locked, unable to log in')
                else:
                    print('No User')

    def input(self):
        if self.teacher_flag:
            #f = open('achievement.txt','a')
            c = input('Please input Chinese achievement:')
            m = input('Please input Mathematics achievement:')
            e = input('Please input English achievement:')
            #f.write('{} :Chinese {},Mathematics {},English {}.'.format(self.input_name,c,m,e))
            self.achievement[self.input_name] = c,m,e
            print(self.achievement)

    def query(self):
        name = input('Please input the name :')
        if name in self.achievement:
            if self.student_flag or self.teacher_flag:
                c, m, e = self.achievement[name]
                print('{} :Chinese {},Mathematics {},English {}.'.format(self.input_name,c,m,e))
                self.query()
        elif self.teacher_flag:
            x = input("Enter the user's score yes or not?:")
            if x == 'yes':
                self.input_name = name
                self.input()
            elif x == 'no':
                y = input('Continue to query yes or no?:')
                if y == 'yes':
                    self.query()
        else:
            x = input("Can't found.Enter the user's score yes or not?")
            if x == 'yes':
                self.query()

q = Query()
q.sign_in()