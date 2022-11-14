'''
random
-0.0~0.9범위를 지정해서 특정 범위의 무작위 수를 가져온다.

'''

# import random
# for i in range(5):
#     print(random.random(), end= " ")
# print()

# for i in range(5):
#     print(int(random.random()*3), end=" ")
# print()

# for i in range(5):
#     print(random.randrange(0,3), end=" ")

#로또프로그램 생성
#1~45 사이의 무작위 중복되지 않는 6개의 수
'''
import random

s = set()

for i in range(6):
    num = random.randrange(1,45)
    s.add(num)
print(s)

'''
import random

ls = []
while len(ls) < 6:
    num = random.randrange(1,46)
    if ls.count(num) == 0:
        ls.append(num)
ls.sort()
print( ls )

#updown게임 만들기

import random

com = None
cnt = 1
newcnt = 1

while True:
    print('{:=^30}'.format('updown게임'))
    print('1. 게임시작 2. 최고기록확인 3. 종료')
    opt = int(input('옵션을 선택하세요 : '))
    if opt == 1:
        com = random.randrange(1,100)
        print('컴퓨터가 1부터 100 사이의 숫자를 골랐습니다.')
        while True:
            user = int(input('수 입력 :'))
            cnt += 1
            if user == int(com):
                print(f'정답! 컴퓨터의 숫자는 {int(com)} 이었습니다!')
                if newcnt < cnt:
                    newcnt = cnt
                    print(f'기록갱신! 당신의 최고기록은 {newcnt}회 입니다.') 
                break
            elif user < int(com):
                print('up')
            elif user > int(com):
                print('down')
    elif opt == 2:
        if com == None:
            print('게임을 먼저 시작해주세요.')
        else:
            print(f'당신의 최고기록은 {cnt}회 입니다.')
    elif opt == 3:
        print('종료합니다.')
        break
    else:
        print('옵션을 다시 선택해주세요.')

#야구게임
# import random

# s = set()
# cnt = 0
# while True:
#     print('{:=^30}'.format('야구게임'))
#     print('1. 게임시작 2. 최고기록확인 3. 종료')
#     opt = int(input('옵션을 선택하세요 : '))
#     if opt == 1:
#         while com < 3:
#             com = random.randrange(1,10)
#             s.add(com)
#             print('컴퓨터가 숫자를 선택했습니다.')
#             num1 = int(input('첫번째 숫자를 입력하세요.'))
#             num2 = int(input('두번째 숫자를 입력하세요.'))
#             num3 = int(input('세번째 숫자를 입력하세요.'))

#     elif opt == 2:
#         pass
#     elif opt == 3:
#         print('게임을 종료합니다.')
#         break
#     else:
#         print('옵션을 다시 선택해주세요.')