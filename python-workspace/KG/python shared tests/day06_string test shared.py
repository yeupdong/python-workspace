#숫자 2개로 이뤄진 복권 출력 프로그램 
#랜덤 숫자와 사용자 입력 숫자 비교 
#2자리 숫자 일치 : 100만원  
#1자리 숫자 일치 : 50만원 

# import random
# com = random.randrange(1,100)

# user = int(input('복권번호를 입력하세요. (0~99사이의 값만 입력 필수):'))
# print("당첨번호는",com,"입니다")

# num1 = com//10 #컴퓨터 번호
# num2 = com % 10
# num3 = user//10 #사용자 입력 번호
# num4 = user % 10

# if num1 == num3 and num2 == num4:
#     print('축하합니다. 당신의 상금은 100만원입니다.')
# elif num1 == num3 or num2 == num4:
#     print("축하합니다. 당신의 상금은 50만원입니다.")
# else:
#     print("꽝 입니다. 다시 도전해주세요")


# from random import randrange
# import os
# from time import sleep
# li=['고양이', '강아지', '거북이', '토끼', '뱀', '사자', '호랑이', '표범', '치타', '하이에나', '기린', '코끼리', '코뿔소', '하마', '악어', '펭귄', '부엉이', '올빼미', '곰', '돼지', '소', '닭', '독수리', '타조', '고릴라', '오랑우탄', '침팬지', '원숭이', '코알라', '캥거루', '고래', '상어', '칠면조', '직박구리', '쥐', '청설모', '메추라기', '앵무새', '삵', '스라소니', '판다', '오소리', '오리', '거위', '백조', '두루미', '고슴도치', '두더지', '우파루파', '맹꽁이', '너구리', '개구리', '두꺼비', '카멜레온', '이구아나', '노루', '제비', '까치', '고라니', '수달', '당나귀', '순록', '염소', '공작', '바다표범', '들소', '박쥐', '참새', '물개', '바다사자', '살모사', '구렁이', '얼룩말', '산양', '멧돼지', '카피바라', '도롱뇽', '북극곰', '퓨마', '미어캣', '코요테', '라마', '딱따구리', '기러기', '비둘기', '스컹크', '돌고래', '까마귀', '매', '낙타', '여우', '사슴', '늑대', '재규어', '알파카', '양', '다람쥐', '담비']
# best = -1
# while True:
#     os.system('cls')
#     print("동물들 이름으로 타자 게임")
#     print("1.게임시작")
#     print("2.최고기록")
#     print("3.종료")
#     n=input(">>>")
    
#     if n=='1':
#         cnt=0
#         i=0
#         while True:
#             i+=1
#             animal=li[randrange(1,100)]
#             os.system('cls')
#             print(animal)
#             sleep(0.5)
#             os.system('cls')
#             answer = input("정답>>>")
#             if animal == answer:
#                 cnt+=1
#             if i==10:
#                 if best < cnt:
#                     best = cnt
#                 print("총 정답수:",cnt)
#                 os.system('pause')
#                 break

#     elif n=='2':
#         if best == -1:
#             print("게임부터 시작하세요")
#         else:
#             print(f"최고기록은 {best}번 입니다.")
#         sleep(1)
#     elif n=='3':
#         print("프로그램이 종료됩니다.")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")
#         sleep(1)


# 아래 문자열에 대문자기준으로 문장 줄바꿈 추가
# line='Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day'
# 출력 결과
# Have a nice day 
# Have a nice day 
# Have a nice day 
# Have a nice day 
# Have a nice day 
# Have a nice day 


line='Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day'
i=0
while True:
    if i!=0 and line[i].isupper():
        print()
    print(line[i],end='')
    i += 1
    if i == len(line):
        break