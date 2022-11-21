'''
class

- 틀, 틀안에 모든 기능과 변수가 존재한다.
- 함수들을 모아놓은 틀.
- 하나의 자료형이다.
- 이름을 지정할때 첫 자는 무조건 대문자.
- "."은 멤버접근연산자

객체
- 클래스 자료형으로 변수를 만들면 객체라고 표현한다.

메소드
- 클래스안에 함수를 만들면 메소드라 칭한다.

객체지항
- 처리 속도가 느리다. 무겁다.
- 한번에 처리가 가능해서 더 편리하다.

절차지항
- 각각의 함수별로 존재하는 것.
- 처리 속도가 빠르다.
- 그러나 사용 용이성이 객체지항보다 떨어진다.
'''
# #클래스 object(객체) 생성
# class Info:
#     name = None
#     age = None
#     address = None
    
# #객체값 지정하기 (객체: name, age, address)
# i = Info()
# i.name = "홍길동"
# i.age = 20
# i.address = "산골짜기"
# print(i.name, i.age, i.address )    #출력값: 홍길동 20 산골짜기

# #class
# def test():
#     info = Info()
#     info.name = "테스트"
#     print(info.name)

# def test1():
#     info = Info()
#     info.name = "연습중"
#     print( info.name )
# test()                              #출력값: 테스트
# test1()                             #출력값: 연습중


class MyClass:
    def test(self):
        print("test method")
        print(self)                   #출력값: <__main__.MyClass object at 0x000002523C973D50>
c = MyClass()
c.test()


# ex 1) 두 수 입력받아서 합 출력 (3가지 함수정의하기!)
class MethodTest01:
    def myInput(self):  #입력받는 함수
        n1 = int(input('수 입력 :'))
        n2 = int(input('수 입력 :'))
        return n1, n2

    # def sumFunc(self):
    #     n1 = int(input('수 입력 :'))
    #     n2 = int(input('수 입력 :'))
    #     s = n1 + n2
    #     print('합 :', s)

    def sumN(self,n1,n2):   #연산하는 함수
        return n1+n2
    
    def myPrint(self, *t):  #출력하는 함수
        print(f'{t[0]}+{t[1]}={t[2]}')


obj = MethodTest01() #클래스호출
#obj.sumFunc() #객체호출
n1, n2 = obj.myInput()
s = obj.sumN(n1,n2)
obj.myPrint(n1, n2, s)

# quiz 1) 입력,출력,연산메소드 만들기
# 1. 두 수를 입력 받아 큰 수 출력하는 class
# 2. 입력받은 수가 짝/홀수 판별하는 class
# 3. 입력받은 수가 3의배수인지 아닌지 판별하는 class
# 4. 수를 입력 받아 소수인지 아닌지 판별하는 class
# 5. 수를 입력 받아 절대값으로만 출력되는 class


class quiz():
    def myInput(self):  # 입력받는 메소드
        num=int(input('수 입력 : '))
        return num
    def maxNum(self, *n): # 큰 수 판별 메소드
        if n[0]>n[1]:
            return n[0]
        else:
            return n[1]
    def display(self, x):   # 출력 메소드
        print('-->', x)
    def evenOdd(self, n):     # 짝/홀 판별 메소드
        if n % 2 == 0:
            return 'even'
        else:
            return 'odd'
    def multiThree(self, n):   # 3의배수 판별 메소드
        if n % 3 == 0:
            return '3의 배수 입니다.'
        else:
            return '3의 배수가 아닙니다.'
    def primeNum(self, n):     # 소수 판별 메소드
        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
        if cnt == 2:
            return '소수입니다.'
        else:
            return '소수가 아닙니다.'
    def absNum(self, n):       # 절댓값 출력 메소드
        if n < 0:
            return -n
        else:
            return n


# 1. 
print('====큰 수 출력====')
ans1 = quiz()
n1 = ans1.myInput()
n2 = ans1.myInput()
maxNum = ans1.maxNum(n1, n2)
ans1.display(maxNum)

# 2.
print('====짝/홀 판별====')
ans2 = quiz()
n = ans2.myInput()
print(ans2.evenOdd(n))

# 3.
print('====3의배수 판별====')
ans3 = quiz()
n = ans3.myInput()
print(ans3.multiThree(n))

# 4.
print('====소수 판별====')
ans4 = quiz()
n = ans4.myInput()
print(ans4.primeNum(n))

# 5.
print('====절댓값 출력====')
ans5 = quiz()
n = ans5.myInput()
abs = ans5.absNum(n)
ans5.display(abs)

