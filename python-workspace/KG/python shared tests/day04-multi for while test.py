#피라미드 만들기

#중첩반복문을 활용하여 피라미드 만들기. 숫자를 받아와서(변수) 피라미드의 높이를 정하고 피라미드를 쌓자.

#힌트
#피라미드를 나타내는 변수는 꼭 숫자가 아니어도 된다. (높이를 나타내는 변수는 무조건 숫자여야 함.)
#첫번째 반복문 = 피라미드의 층수(높이)가 될 것이다.
#두번째 반복문 = 공백이 될 것이다.
#세번째 반복문 = (모양)이 될 것이다. 
#두번째와 세번째 반복문은 indentation(공백)이 같은 위치에 있다.
#분명 문제가 겹칠 것이다. 다른 조 문제들을 보다보면 또 다른 힌트가 있겠지...


# num = int(input('피라미드의 높이'))
# pyramid = ''

# for i in range(1,num+1):
#     for k in range(num,i,-1):
#         pyramid+=' '
#     for k in range(0,2*i-1):
#         pyramid+='□'
#     pyramid += '\n'
# print(pyramid)

# 중국집 메뉴판 만들기
# 다음과 같이 메뉴판을 만들고, 총 주문 금액과 총액 출력하기

# ========중국집 메뉴판========
#1. 자장면 : 6000원
#2. 짬뽕 : 7000원
#3. 볶음밥 : 8000원
#4. 탕수육 : 20000원
#5. 실행 종료

# print(f'{"중국집 메뉴판":=^30}')
# print('1. 자장면 : 6000원')
# print('2. 짬뽕 : 7000원')
# print('3. 볶음밥 : 8000원')
# print('4. 탕수육 : 20000원')
# print('5. 주문완료')
# cash = 0
# jja = 6000
# jjam = 7000
# bok = 8000
# tang = 20000
# while True:
#     option = int(input('무엇을 주문하시겠습니까? :'))
#     if option == 5:
#         print('주문을 마치겠습니다.')
#         print('총 금액은 {:,}원 입니다.'.format(cash))
#         break
#     elif option == 1:
#         cash+=jja
#         print('자장면 1개 추가')
#         print('현재금액은 {:,}원 입니다.'.format(cash))
#     elif option == 2:
#         cash+=jjam
#         print('짬뽕 1개 추가')
#         print('현재금액은 {:,}원 입니다.'.format(cash))
#     elif option == 3:
#         cash+=bok
#         print('볶음밥 1개 추가')
#         print('현재금액은 {:,}원 입니다.'.format(cash))
#     elif option == 4:
#         cash+=tang
#         print('탕수육 1개 추가')
#         print('현재금액은 {:,}원 입니다.'.format(cash))
#     else:
#         print('잘못입력하셨습니다. 1번부터 5번 중에서 다시 선택해주세요.')

# '''
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 

# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
#  - 00시 00분 03초
#  - 00시 13분 30초
#  3이 하나도 포함되어 있지 않아 세면 안 되는 시각
#  - 00시 02분 55초
#  - 01시 27분 45초
# '''

# n = int(input('숫자를 입력하세요. :'))
# cnt = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 cnt+=1
# print(f'{n}시59분59초까지 "3"이 포함된 시간은 총{cnt}회 입니다.')

# (1분미만)스탑워치 만들기
# 스탑워치 작동할 시간(초)을 입력 받습니다. 이때 시간은 60초 미만의 초단위로 받습니다.
# 스탑워치 작동시작과 동시에 화면에는 시계화면만 출력되도록 합니다. (이전의 출력내용들을 지우기)
# 스탑워치 시계화면은 1/60초 단위로 증가하며 ' (초) : (0.1초) ' 로 표시합니다.
# 스탑워치 시작은 ' 0 : 0 '       ex) 0 : 0 -> 0 : 1 
# 0 : 59 다음은 0 : 60 이 아닌 1 : 0 로 출력합니다.     ex) 0 : 59 -> 1 : 0 , 1 : 59 -> 2 : 0
# 시계화면은 고정된 채 시간만 변하도록 합니다. 
# (1/60초 단위로 쭉 출력되지 않고, 디지털 시계처럼 '00:00'의 틀은 유지한 채 숫자만 변하도록 )
# 스탑워치가 종료되면 종료된 시계와 종료 알림 문구를 출력합니다. (시계화면을 지우지 말 것) 
## os.system('cls') 사용시 출력화면이 너무 빠르게 지워지므로 1/60초간 시간을 보이게 하기 위해 time모듈의 sleep함수를 사용합니다.

# 풀이코드

# import os
# from time import sleep
# print('{:=^}'.format('1분미만 제한 스탑워치'))
# time=int(input('스탑워치 시간 입력(초) >>> '))
# if time >= 60:
#     print('제한 시간을 초과했습니다.')
# else:
#     os.system('cls')
#     print(' 0 : 0 ')
#     for s in range(0, time):
#         for ms in range(1, 60):
#             os.system('cls')
#             print(f' {s} : {ms} ')
#             sleep(1/60)       # Delay for 1 second
#             if ms == 59:
#                 os.system('cls')
#                 print(f' {s+1} : 0 ')
#                 sleep(1/60)       # Delay for 1 second
#     print(f'\n{time}초 스탑워치를 종료합니다.')

#[문제3. ]
#덧셈 뺼셈 곱셈 나눗셈 몫 나가기가 되는 계산기를 만들어보자.

# print("{:=^50}".format("Calculator"))
# print('1. Addition\t 2. Substraction\t 3. Muliplication\t 4. Divide\t 5. End calculator')
# print("="*50)

# while True:
#     a = int(input('Please enter your first chosen number.'))
#     option = int(input('Please choose your option.'))
#     b = int(input('Please enter your second chosen number.'))
#     if option == 5:
#         print('End calculator')
#         break
#     elif option == 1:
#         print(f'The answer is {a+b}.')
#     elif option == 2:
#         print(f'The answer is {a-b}.')
#     elif option == 3:
#         print(f'The answer is {a*b}.')
#     elif option == 4:
#         print(f'The answer is {a/b}.')
#     else:
#         print('Please try again.')

#임의의 숫자 n을 입력받아 맞추는 프로그램을 작성하시오.


cnt = 1
num = int(input('Please select one number between 1~100 : ')) #어떻게 하면 1~100의 숫자를 고르지 않았을 때 다시 선택하라고 할지 생각해보기
while True:
    i = int(input('Search for a number : '))
    if i == num:
        print('Correct!')
        print(f'You had {cnt} chances to get the answer.')
        break
    elif i < num:
        print('Up. Please try again.')
        cnt+=1
    elif i > num:
        print('Down. Please try again.')
        cnt+=1
