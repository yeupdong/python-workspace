class AAA:
    def test1(self):
        print("test1")
        print(self.num)
a = AAA()
a.num = 12345
a.test1()               #출력값: test1\n12345

print("="*20)

class BBB:
    aaa = "안녕하세요"   #해당 클래스 이름으로 접근한다.
    def test1(self):
        print("test1")
        #print(aaa)     #지역변수로 인식
b = BBB()
b.test1()               #출력값: test1 의미: BBB(test1)

print("="*20)

class BBB:
    aaa = "안녕하세요"   #해당 클래스 이름으로 접근한다. 클래스의 변수는 객체를 만들어줘야만 인식이 된다.
    def test1(self):
        print("test1")
        print(self.aaa) #지역변수로 인식
b = BBB()               #출력값: 안녕하세요
b.test1()               #출력값: test1 의미: BBB(test1)

print("="*20)

class BBB:
    aaa = "안녕하세요"   #해당 클래스 이름으로 접근한다.
    def test1(self):
        print("test1")
        print(self.aaa) #지역변수로 인식
        print(BBB.aaa)
b = BBB()               
b.test1()               #출력값: test1\n안녕하세요\n안녕하세요

print("="*20)

class BBB:
    aaa = "안녕하세요"   #해당 클래스 이름으로 접근한다.
    def test1(self):
        print("test1")
        print(self.aaa) #지역변수로 인식
        print(BBB.aaa)
print(BBB.aaa)          #출력값: 안녕하세요 #해당 변수에 접근을 하려면, 클래스 이름으로 접근한다. (클래스.변수)

BBB.num = "넘입니다"
print(BBB.num)          #출력값: 넘입니다

b = BBB()
b.bbb = "bbb입니다"     #bbb는 인스턴스변수로 생성이 됨. 의미: BBB(bbb)
#print( BBB.bbb)        #에러발생 type object 'BBB' has no attribute 'bbb'
print(b.bbb)            #출력값: bbb입니다

def test():     
    b = BBB()           #지역변수
    b.test1()   
test()                  #출력값: test1\n안녕하세요\n안녕하세요

print("="*20)

class CCC:
    a = 'aaaa'
    def test():
        print("test입니다")
    def test1(self):
        print("self입니다")

CCC.test()              #출력값: test입니다 class method는 class이름으로 접근
#CCC.test1()            #에러발생 CCC.test1() missing 1 required positional argument: 'self'
c = CCC()               #출력값: test입니다
c.test1()               #출력값: self입니다
#c.test()               #에러발생 CCC.test() takes 0 positional arguments but 1 was given

'''
생성자

- 객체가 만들어질 때 자동으로 호출되는 메소드
- __init__(self)이름을 사용한다.
- 일반적으로 변수 초기화 목적으로 사용한다.
'''

#__init__(self) 생성자 연습
class TestClass:
    def __init__(self):
        print("생성자 실행")
t = TestClass()         #출력값: 생성자 실행

print("="*20)

#__init__(self) 생성자와 일반호출방법 비교
class TestClass:
    def __init__(self):
        print("생성자 실행")
    def test(self):     #일반적인 생성방법
        pass
t = TestClass()         #출력값: 생성자 실행
t.test()                #출력값: 생성자 실행

print("="*20)

#__init__(self) 생성자 연습 2
class TestClass02:
    def __init__(self,name):
        self.name = name
    def printName(self):
        print("당신의 이름은 : ",self.name)
n = input("이름 입력 :")
t = TestClass02(n)
t.printName()

print("="*20)

#__init__(self) 생성자 연습 3
class TestClass03():
    def __init__(self,version,memory):  #호출을 따로 안해줘도 자동호출이 된다.
        self.version = version
        self.memory = memory
    def printM(self):
        print("버전 : ",self.version)
        print("메모리 : ",self.memory)
t = TestClass03("win10", "8GB")         #초기설정값
t.printM()

print("="*20)

class TestClass03():
    def __init__(self,version,memory):
        self.version = version
        self.memory = memory
    def setVersion(self,version):       #호출값이 있어야 호출이 된다.
        self.version = version
    def printM(self):
        print("버전 : ",self.version)
        print("메모리 : ",self.memory)
t = TestClass03("win10", "8GB")         #초기설정값
t.setVersion("버전 정보")
t.printM()

print("="*20)

class TestClass03():
    def __init__(self,version,memory):  #호출을 따로 안해줘도 자동호출이 된다.
        self.version = version
        self.memory = memory
    def printM(self):
        print("버전 : ",self.version)
        print("메모리 : ",self.memory)
    def __str__(self):
        #return "원하는 값 표현"
        return f"{self.version},{self.memory}"
t = TestClass03("win10", "8GB")         #초기설정값
t.printM()
print("t : ", t)

print("="*20)


# ex 2 ) 컴퓨터 기능 실행 프로그램 만들기 (계산기, 메모장)

import os
class Computer:
    def __init__(self , version={}, function={} ):
        self.version = version
        self.function = function
    def printVersion(self):
        print( "사양을 보여 줍니다" )
        print("------------------")
        for k, v in self.version.items() :
            print(k,":",v)
        print("------------------")
    def printFunction(self):
        print( "기능을 보여 줍니다" )
        print("------------------")
        for k, v in self.function.items() :
            print(k,":",v)
        print("------------------")
        value = input("사용할 기능 입력 : ")
        os.system(self.function[value])
        
version = {"cpu":'i7' , "memory":'8'}
function = {"계산기":"calc", "메모장":"notepad"}
com = Computer(version, function)
while True:
    print("1. version확인")
    print("2. 기능 확인")
    print("3. 종료")
    num = int( input(">>> : ") )
    if num == 1:
        com.printVersion()
    elif num == 2:
        com.printFunction()
    else:
        break
