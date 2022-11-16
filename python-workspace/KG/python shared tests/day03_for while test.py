# 좌석 예약 프로그램
# 총 30개의 좌석에 예약인원에 맞는 좌석을 지정해주는 프로그램입니다.
# 일행 수(people)를 입력받고, 일행 수가 남은 좌석 수 이하인 경우 지정좌석(reserved)을 알려줍니다.
# 좌석은 1번부터 순차적으로 지정합니다.
# 좌석을 알려준 후 남은 좌석 갯수를 알려주고 예약을 계속합니다.
# 남은 좌석이 없는 경우 프로그램을 종료합니다.
# hint : 변수 초기값(예약된 좌석 reserved=0, 전체 좌석 seat=30, 예약 가능 좌석 possible=30)
# 출력 예시
# ==========좌석 예약 프로그램==========
# 일행 수 입력 : 5
# + --------------------- +
# | 1부터 5번 좌석입니다. |
# + --------------------- +
# 예약 가능 25자리 남았습니다.

# ==========좌석 예약 프로그램==========
# 일행 수 입력 : 6
# + --------------------- +
# | 6부터 11번 좌석입니다. |
# + --------------------- +
# 예약 가능 19자리 남았습니다.

# ==========좌석 예약 프로그램==========
# 일행 수 입력 : 19
# + --------------------- +
# | 12부터 30번 좌석입니다. |
# + --------------------- +
# 예약 가능 0자리 남았습니다.

# 모든 좌석이 예약되었습니다. 예약을 종료합니다.

# audiences = 0
# vacant = 30
# booking = 0
# while True:
#     print(f'{"좌석 예약 프로그램":=^50}')
#     audiences = int(input('총 관객이 몇명입니까? :')) # 6
#     if audiences <= vacant:
#         print(f'{booking+1}부터 {booking+audiences}까지 예약되었습니다.') # 1 ~ 6
#         booking += audiences # booking = 0 + 6 => 6
#         vacant = vacant - audiences # vacant = 30 - 6 => 24
#         print(f'{vacant}개의 자리가 남아있습니다.')
#     elif vacant == 0:
#         print('자리가 더 이상 없습니다.')
#         break
#     elif audiences > vacant:
#         print('충분한 자리가 없습니다. 다시 시도해 주세요.')
#         print(f'{vacant}개의 자리가 남아있습니다.')

# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
# num = int(input('아무숫자챌린지'))
# for i in range(1,10):
#     print(f'{num}*{i}={num*i}')

# #양의정수 n을 입력받고 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, n번째 줄에는 별 n개를 출력하시오.
# n = int(input('아무숫자챌린지 :'))
# i = 0
# while i < n:
#     i += 1
#     print('*'*i)

#첫날 10원을 입금하고 그 다음날 부터 2배씩 30일동안 저축을한다면 저축된 금액은 얼마인가?
# first = 10
# save = 0
# for i in range(31):
#     save+=first # save = save + first = 10
#     first*=2 # first = first * 2 = 20
# print(f'{save:,}')

#N값을 입력 받아 1부터 N까지의 수 중에서 소수를 구하는 프로그램을 작성하시오.
#소수 : 1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수
#소수 배수가 없는 수

# n = int(input('숫자를 입력하세요 :'))
# for i in range(1,n+1):
#     if i != 1 and i // i < 2:
#         print(i)

# import os
# sum_ = 0
# i = 0
# while True:
#     print('='*40)
#     print('1. 입력한 수까지의 합 계산 시작!')
#     print('2. 끝내고 싶어!')
#     print('='*40)
#     o = int(input('옵션: '))
#     if o == 1:
#         n = int(input('입력: '))
#         for i in range(0,n+1):
#             i += 1
#             sum_ += i
#         print(sum_)
#     if o == 2:
#         os._exit(1)

# sum_ = 0

# for i in range(4,22):
#     if i % 2 != 0:
#         sum_ += i
# print(sum_)

# i = 0
# x = int(input('별이 몇개? : '))
# for i in range(0,x):
#     i += 1
#     print('*'*i)

import os
os.system("cls") 
n = None
while True :
    print('='*40)
    print('1. 숫자 입력 (0 ~ 99)')
    print(f'2. 사이클 횟수 확인 (현재 숫자 : {n})')
    print(f'3. 사이클 과정 확인 (현재 숫자 : {n})')
    print('4. 종료')
    print('='*40)
    num = int(input('>>>>>'))
    if num == 1 :
        N = int(input('숫자를 입력하세요 : '))
        print()
        n = N
        time = 0
        while True :
            if 99 < N or N < 0 :
                print('잘못된 숫자를 입력하셨습니다.')
                N = int(input('숫자를 입력하세요 : '))
                print()
            elif 0 <= N < 100 :
                new = (N//10) + (N%10)
                N = ((N%10)*10) + (new%10)
                time += 1
            if N == n :
                break

    elif num == 2 :
        print(f'{n}의 사이클횟수는 {time}회 입니다')
        os.system("pause")
        print()

    elif num == 3 :
        print(f'최초숫자A : {N}')
        new = (N//10) + (N%10)
        print(f'새로운수B : {N//10} + {N%10} = {new}')
        print(f'{(N%10)} {new%10}<------------┘----┘')
        N = ((N%10)*10) + (new%10)
        time = 1
        print(f'{time}회')
        print()
        while True :
            print(f'기준숫자A : {N}')
            new = (N//10) + (N%10)
            print(f'새로운수B : {N//10} + {N%10} = {new}')
            print(f'{(N%10)} {new%10}<------------┘----┘')
            N = ((N%10)*10) + (new%10)
            time += 1
            print(f'{time}회')
            print()
            if N == n :
             break
        os.system("pause")
        print()
    
    
    elif num == 4 :
        break
    os.system("cls") 