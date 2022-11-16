'''
#변수

- 데이터를 저장하기 위한 공간
- 언제든지 변경이 가능하다.

#변수 이름 작성 규칙

- 의미를 부여해서 만든다.
- 이름은 영어로 만든다.
- 보통 3~10자 이내에 만든다.
- 키워드는 사용하면 안된다.(sum, input등등)
'''
import keyword
print( keyword.kwlist)
#대입연산자
num = 100 #오른쪽 결과값을 왼쪽식에 대입.
print( num )
print( 100 )
print('\t')
print('\t')
n = 5
print('변경 전 n:',n)
n = n+10
print(f'변경 후 n: {n}') #n = n(5) + 10
print('\t')
print('\t')
n1 = 5; n2 = 10
sum_ = n1 + n2
print(f'{n1}+{n2}={sum_}')
print('\t')
print('\t')
#Question
num1 = 10
num2 = 20
sum_ = num1 + num2
print('num1({})+num2({})={}'.format((num1),(num2),sum_)) #format을 이용하여 표현
print(f'num1({num1})+num2({num2})={sum_}') #format을 이용하여 표현
print("num1(",num1,") + num2'(",num2,") =",sum_) #,를 이용하여 표현
print('\t')
print('\t')
#round
flt = 123.456
print('flt :', flt)
print('round(flt) :', round(flt))
print('round(flt,1) :', round(flt,1)) #소수점 첫번째 자리수까지 표현
print('round(flt,2) :', round(flt,2)) #소수점 두번째 자리수까지 표현
#Question
py = 97
c = 67
java = 78
sum_ = py + c + java
avg = sum_/3
print(round(avg,2))
stn = 11
time = 37
avg = time / stn
print(round(avg,2))
flr = 2.6
one = 5.0023
cnt = 14
height = ((cnt-1)*flr)+one
print(round(height,3))

a = int(input('python점수를 입력하시오 :'))
b = int(input('c언어 점수를 입력하시오 :'))
c = int(input('java 점수를 입력하시오 :'))
avg = (a+b+c)/3
print(round(avg,2))
