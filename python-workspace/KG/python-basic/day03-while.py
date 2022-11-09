import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#import 는 현재 프로젝트로 다른 위치에 있는 특정 기능을 가져오는 명령어.

import os

#while 조건식:
#    종속문장 (조건식이 True면 계속해서 반복한다.)
#===================================================
# data = 0 #해당 식이 없이 아래의 반복문을 실행했을 시, data값이 없기 때문에 2번에서 오류가 발생한다. 
# data = None

# while True:
#     print('='*30)
#     print('1.데이터 입력')
#     print('2.데이터 출력')
#     print('3.종료')
#     print('='*30)
#     num = int(input('>>> :'))
#     if num == 1:
#         data = input('데이터 입력 :')
#     elif num == 2:
#         if data == None:
#             print('There is no saved data.')
#         else:
#             print('입력데이터 :',data)
#         os.system('pause')
#     elif num == 3:
#         os._exit(1)
#     os.system('cls')
#=============================================================

while True:
    print('='*30)
    print('MENU')
    print('='*30)
    print("1. Input student's name")
    print("2. Input three subjects' marks (kor, eng, math)")
    print("3. Output student's name")
    print("4. Output total marks")
    print("5. Output average marks")
    print("6. End")
    print('='*30)
    num = int(input('Input your option. :'))
    if num == 1:
        data = input('Input you name. :')
    elif num == 2:
        if data == 0:
            print('Please go back to 1 and enter your name.')
        else:
            kor = int(input('Please enter your mark of kor. :'))
            eng = int(input('Please enter your mark of eng. :'))
            math = int(input('Please enter your mark of math. :'))
    elif num == 3:
        if data == 0:
            print('Please go back to 1 and enter your name.')
        else:
            print('Student name :', data)
    elif num == 4:
        total = kor + eng + math
        print(f'Total mark of three subjects is {total}.')
    elif num == 5:
        avg = total / 3
        print(f'Average marks of three subjects is {round(avg,2)}')
    elif num == 6:
        print("End system")
        break
