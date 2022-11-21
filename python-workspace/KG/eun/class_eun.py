'''
class : - 틀 안에 모든 기능과 변수 존재
        - 하나의 자료형
        - object(객체) : 클래스안의 변수
        - method(메소드) : 클래스안의 함수
'''
# 클래스 object(객체) 생성
class Info:
    name = None
    age = None
    id = None
    score = None

# object(객체)값 지정하기 (object(객체) : Info 안의 name, age, ..)
user = Info()
user.name = '홍길동'
user.age = 20 
user.id = 'aaa'
print(user.name, user.age, user.id)

# 함수에서 class 사용
def test():
    student = Info()
    student.name = '김개똥'
    print(student.name)

test()  # 김개똥

# 클래스 method(메소드) 생성
class myClass:
    def test(self):     # test : method(메소드)
        print('test method(메소드) 입니다.')
        print(self) # <__main__.myClass object at 0x000001B37BA93B50>

# 클래스 method(메소드) 사용  (method(메소드) : class 안의 함수인 test)
c = myClass()
c.test()

# ex 1 ) 두 수 입력받아서 합 출력 (3가지 함수정의하기!)
class methodTest:
    def myInput(self):  # 입력받는 함수
        n1=int(input('수 입력 :'))
        n2=int(input('수 입력 :'))
        return n1, n2
    def numSum(self, n1,n2):   # 덧셈하는 함수
        return n1+n2
    def sumDisplay(self, *t):  # 결과 출력 함수
        print(f'{t[0]} + {t[1]} = {t[2]}')

obj = methodTest()
num1, num2 = obj.myInput()
sum_ = obj.numSum(num1, num2)
obj.sumDisplay(num1, num2, sum_)


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


