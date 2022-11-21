'''
상속
- 이미 만들어진 코드를 상속 받는 것
- 상속받으면 상속받은 코드를 사용할 수 있다.

Overriding
- 같은 메소드가 있으면 자기 자신에게 있는 메소드를 실행한다. 
- 패치하고자 하는 내용이 있으면 사용한다.

super()
- 같은 메소드가 있을 때, 부모가 갖고 있는 내용을 찾아감. 
'''

class Calc:
    def calc(self):
        print("부모 나는 계산기야~")
c = Calc()
c.calc()

class Computer(Calc):   #상속받고자 하는 클래스를 괄호안에 넣어준다. 자기자신한테 해당 메소드가 없으면, 상속을 주는 클래스로 찾아가 메소드를 찾는다. 
    def calc(self):
        print("아들 나는 계산기야~")
    def computer(self):
        print("computer")
c = Computer()
c.computer()
c.calc()


class Computer(Calc):   #상속받고자 하는 클래스를 괄호안에 넣어준다. 자기자신한테 해당 메소드가 없으면, 상속을 주는 클래스로 찾아가 메소드를 찾는다. 
    def calc(self):
        print("아들 나는 계산기야~")
    def computer(self):
        print("computer")
        self.calc() #super.calc = 부모가 가지고 있는 메소드를 찾아감.
c = Computer()
c.computer()
#c.calc()

print("="*20)

class MemberInfo:
    def inputMember(self, m):
        self.name = input("이름 입력 : ")
        self.age = input("나이 입력 : ")
        self.add = input("주소 입력 : ")

class Display:
    def display(self):
        self.mem = MemberInfo()
        self.mem.inputMember()
        #print(self.mem.name)
        mem_dic = {}
        mem_dic[self.mem.name] = self.mem
        print(mem_dic)
d = Display()
d.display()

print("="*20)

class Display:
    def display(self):
        mem_dic = {}
        for i in range(3):
            self.mem = MemberInfo()
            self.mem.inputMember()
            #print(self.mem.name)
            mem_dic[self.mem.name] = self.mem
        print("--- 내용출력 ---")
        for k,v in mem_dic.items():
            #print(v)
            print(k,":",v.age)
            print(v.name)
            print(v.age)
            print(v.add)
            print("-----")
        # print(mem_dic)
        # print(mem_dic[self.mem.name])
        # print(mem_dic[self.mem.name].name)
        # print(mem_dic[self.mem.name].age)
        # print(mem_dic[self.mem.name].add)
d = Display()
d.display()


class MemberInfo:
    def inputMember(self, m):
        self.name = input("이름 입력 : ")
        self.age = input("나이 입력 : ")
        self.add = input("주소 입력 : ")
    def __str__(self):
        return f'이름[{self.name}]\n나이[{self.age}]'

class Display:
    def display(self):
        self.mem = MemberInfo()
        self.mem.inputMember()
        #print(self.mem.name)
        mem_dic = {}
        mem_dic[self.mem.name] = self.mem.deepcopy()   #deepcopy를 사용하는 경우 self.mem = MemberInfo()를 메소드 밖에 위치.
        print(mem_dic)
        print(mem_dic[self.mem.name])
        print(mem_dic[self.mem.name].name)
        print(mem_dic[self.mem.name].age)
        print(mem_dic[self.mem.name].add)
d = Display()
d.display()


class MemberInfo:
    def inputMember(self, m):
        while True:
            self.name = input("이름 입력 : ")
            if m.get(self.name) != None:
                print("아이디 있음")
                continue
            break
        self.age = input("나이 입력 : ")
        self.add = input("주소 입력 : ")

class Display:
    def display(self):
        mem_dic = {}

        for i in range(3):
            self.mem = MemberInfo()
            self.mem.inputMember(mem_dic)
            #print(self.mem.name)
            mem_dic[self.mem.name] = self.mem
        print("--- 내용출력 ---")

        for k,v in mem_dic.items():
            print(v)
            print(k,":",v.age)
            print(k,":",v.name)
            print(k,":",v.age)
            print(k,":",v.add)
            print("-----")
        print(mem_dic)
        print(mem_dic[self.mem.name])
        print(mem_dic[self.mem.name].name)
        print(mem_dic[self.mem.name].age)
        print(mem_dic[self.mem.name].add)
d = Display()
d.display()

# e x 3 )

# class Membership:
#     def sign_up(self,info={}):
#         self.name = input("이름 입력 : ")
#         while True:
#             self.id = input("아이디 입력 : ")
#             if info.get(self.id) != None:
#                 print("중복된 아이디입니다. 다른 아이디를 입력해주세요.")
#             else:
#                 break
#         self.password = input("비밀번호 입력 : ")

# class Login():
#     def log_in(self, info, user_id, user_password):
#         if info.get(user_id) != None:
#             if info.get(user_id).password == user_password:
#                 return 0
#             else:
#                 return 1
#         return -1

# info = {}
# login = Login()
# while True:
#     print("1.로그인")
#     print("2.회원가입")
#     print("3.모든 사용자 보기")
#     print("4.종료")
#     opt = int(input(">>> : "))
#     if opt == 1:
#         user_id = input("인증할 아이디 입력 : ")
#         user_password = input("인증할 비밀번호 입력 : ")
#         result = login.log_in(info,user_id,user_password)
#         if result == 0:
#             print('인증되었습니다.')
#         elif result == 1:
#             print('비밀번호를 다시 입력해주세요.')
#         else:
#             print('존재하지 않는 아이디 입니다.')
#     elif opt == 2:
#         mem = Membership()
#         mem.sign_up(info)
#         info[mem.id] = mem
#         print('회원 가입을 축하드립니다.')
#     elif opt == 3:
#         print('===모든 사용자 보기===')
#         for k, v in info.items():
#             print('이름 : ', v.name)
#             print('아이디 : ', v.id)
#             print('비밀번호 : ', v.password)
#             print('='*30)
#     elif opt == 4:
#         print('프로그램을 종료합니다.')
#         break
#     else:
#         print('옵션을 다시 입력해주세요.')

# import os
# class Computer:
#     def __init__(self , version={}, function={} ):
#         self.version = version
#         self.function = function
#     def printVersion(self):
#         print( "사양을 보여 줍니다" )
#         print("------------------")
#         for k, v in self.version.items() :
#             print(k,":",v)
#         print("------------------")
#     def printFunction(self):
#         print( "기능을 보여 줍니다" )
#         print("------------------")
#         for k, v in self.function.items() :
#             print(k,":",v)
#         print("------------------")
#         value = input("사용할 기능 입력 : ")
#         os.system(self.function[value])
#     def display(self):   
#         self.version = {"cpu":'i7' , "memory":'8'}
#         self.function = {"계산기":"calc", "메모장":"notepad"}
#         while True:
#             print("1. version확인")
#             print("2. 기능 확인")
#             print("3. 종료")
#             num = int( input(">>> : ") )
#             if num == 1:
#                 self.printVersion()
#             elif num == 2:
#                 self.printFunction()
#             else:
#                 break