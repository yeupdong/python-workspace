'''
클래스 변수
- 클래스가 실행될 때 생성
- 프로그램 내에서 접근 가능
- 프로그램이 종료되지 않는한, 클래스 밖에서도 변수로 활용가능


인스턴스 변수
- 객체가 생성될 때 생성
- 객체를 이용해서만 접근 가능
- 해당 인스턴스 삭제시 변수도 삭제된다


지역변수
- 특정 지역이 실행될 때 생성
- 특정 지역에서만 접근 가능
- 메소드 내에서만
'''

#지역변수 활용하기
class Variable01:
    def var(self):
        v = 100         #지역변수
        print("var v : ",v)
        return
    def var02(self , v):
        print("20 v : ", v)
vv = Variable01()
v = vv.var()
vv.var02(v)             #출력값: var v : 100\n20 v : None

# #클래스 내부에서 동일한 변수를 사용할 시, 지역변수를 사용하기보다는 인스턴스 변수를 사용하는 것이 효과적임. 

print('='*20)

#인스턴스변수 활용하기
class Var02:
    def var(self):
        self.v = 100    #인스턴스변수, 해당 클래스 내부에서 사용가능한 변수 (self로 표현)
        print("var : ",v)
    def var02(self):
        print("20 v :", self.v)
vv = Var02()
vv.var()
vv.var02()              #출력값: var v : None\n20 v : 100

print("="*20)

#인스턴스변수 활용하기(self.머시기)
class Student:
    def inputSt(self):
        self.name = input("이름 입력 : ")   #홍길동
        self.age = input("나이 입력 : ")    #20
    def printSt(self):
        print(self.name, "님")              
        print(self.age, "살")               
s = Student()
s.inputSt()                                 #입력함수 실행
s.printSt()                                 #출력값: 홍길동 님\n20 살

# ex 1 ) 인스턴스변수(self) 활용하기
class Student_Grade:
    def inputSt(self):  #입력받는 함수
        self.name = input("이름 입력: ")                #홍길동
        self.kor = int(input("국어점수 입력 : "))       #90
        self.eng = int(input("영어점수 입력 : "))       #80
        self.math = int(input("수학점수 입력 : "))      #70
    def grade_sum(self):        #연산 함수(합 구하기)
        self.add = self.kor + self.eng + self.math
    def grade_average(self):    #연산 함수(평균 값 구하기)
        self.avg = self.add / 3
    def grade_(self):           #등급매기는 함수
        if self.avg < 70:
            self.grade = "F"
        elif self.avg >= 70 and self.avg < 80:
            self.grade = "C"
        elif self.avg >= 80 and self.avg < 90:
            self.grade = "B"
        elif self.avg >= 90:
            self.grade = "A"
    def printSt(self):          #출력하는 함수
        print(self.name, "님")
        print(f'총 점수는 {self.add}점 입니다.')
        print(f'평균 점수는 {self.avg}점 입니다.')
        print(f'평균 등급은 {self.grade}등급 입니다.')
    
sg = Student_Grade()                        #클래스 호출
sg.inputSt()                                #입력값
sg.grade_sum()                              #240점
sg.grade_average()                          #80.0점
sg.grade_()                                 #B등급
sg.printSt()                                #출력값: 총 점수는 240점 입니다.\n평균 점수는 80.0점 입니다.\n평균 등급은 B등급 입니다.