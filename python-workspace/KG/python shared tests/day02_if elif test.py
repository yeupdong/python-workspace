#문제
'''
Q1. a, b, c는 K 학원에 다니고 있다. 총 훈련일수는 30일이고, 훈련일수의 80%이상을 수강하여야만 출석한 일수 만큼 훈련장려금을 지급 받는다.
1일당 15,800원을 지급 받고, 월 최대 450,000원을 지급 받는다. 
a는 20일, b는 25일, c는 30일 참여했다.
각자가 받게될 훈련장려금을 구하시오. 
단, 소정훈련일수를 채우지 못한 학생은 총 액수를 구할필요 없이'꽁돈 받을 생각만 하지말고 공부 열심히 하거라.' 라고 꾸짖어준다.

Q2. 어느 날, K 학원은 평가(60점 커트라인)를 통과해야만 훈련장려금을 지급을 해준다는 조건을 내걸었다. a는 60점, b는 45점, c는 90점을 받았다. 
Q1에 이어서 위와 같은 조건으로 각자가 지급받은 훈련장려금 액수를 구하시오. 

Q3. S기업은 c에게 관심을 갖고, 일자리를 제안했다. 3년을 일한다면 초봉 4천만원, 2년을 일한다면 초봉 3.5천만원, 1년을 일한다면 초봉 3천만원을 제안했다. 
당신이 c라면 어떤 제안을 받아들일 것인가? 굳이 일 안해도 된다. 

#예시

a는 ()일 출석했고, 총 ()원을 받는다.
b는 ()일 출석했고, 총 ()원을 받는다.
c는 ()일 출석했고, 총 ()원을 받는다.
공부 열심히 하자
'''

# cutline = 30*0.8
# a = 20
# b = 25
# c = 30

# if a > cutline:
#     print(f'a는 {a}일 출석했고, {a*15800}원을 받는다.')
# else:
#     print('꽁돈 받을 생각만 하지말고 공부 열심히 하거라.')
# if b > cutline:
#     print(f'b는 {b}일 출석했고, {b*15800}원을 받는다.')
# if c > cutline:
#     print(f'c는 {c}일 출석했고, {c*15800}원을 받는다.')
# print('공부 열심히 하자.')


# attend_day = 30*8/10
# oneday_pay = 15800
# max_pay=450000
# a, b, c= 20, 25, 30

# if a >= attend_day :
#     if a*oneday_pay <= max_pay:
#         print("a는 {}일 출석했고, 총{}원을 받는다".format(a,a*oneday_pay))
#     else:
#         print("a는 {}일 출석했고, 총{}원을 받는다".format(a,max_pay))
# else:
#     print("공부 열심히 하거라")
# if b >= attend_day :
#     if b*oneday_pay <= max_pay:
#         print("b는 {}일 출석했고, 총{}원을 받는다".format(b,b*oneday_pay))
#     else:
#         print("b는 {}일 출석했고, 총{}원을 받는다".format(b,max_pay))
# if c >= attend_day :
#     if c*oneday_pay <= max_pay:
#         print("c는 {}일 출석했고, 총{}원을 받는다".format(c,c*oneday_pay))
#     else:
#         print("c는 {}일 출석했고, 총{}원을 받는다".format(c,max_pay))
# else:
#     print('꽁돈 받을 생각만 하지말고 공부 열심히 하거라.')

# print('철도 지연 배상금 계산기입니다.')
# tik = int(input('승차권 구매 금액을 입력하세요.'))
# refund = int(input('환불 수단을 선택하세요. 1. 현금 2. 할인증 :'))
# del_min = int(input('지연시간을 입력하세요(분단위로 입력)'))

# if refund == 1:
#     if 40 > del_min >= 20:
#         print(f'지연 배상금은 {"{:,}".format(int(tik*0.125))}원 입니다.')
#     elif 60 > del_min >= 40:
#         print(f'지연 배상금은 {"{:,}".format(int(tik*0.25))}원 입니다.')
#     elif del_min >= 60:
#         print(f'지연 배상금은 {"{:,}".format(int(inttik*0.5))}원 입니다.')
# elif refund == 2:
#     if 40 > del_min >= 20:
#         print(f'지연 배상금은 {"{:,}".format(int(tik*0.25))}원 입니다.')
#     elif 60 > del_min >= 40:
#         print(f'지연 배상금은 {"{:,}".format(int(tik*0.5))}원 입니다.')
#     elif del_min >= 60:
#         print(f'지연 배상금은 {"{:,}".format(tik)}원 입니다.')
# else:
#     print('선택사항을 다시 입력해주세요.')
# ================================================================================
# year = int(input('연도를 입력하세요. :'))
# if year % 4 == 0 and year % 100 != 0:
#     print('윤년입니다.')
# elif year % 400 == 0:
#     print('윤년입니다.')
# elif year % 100 == 0 and year % 400 != 0:1
#     print('윤년이 아닙니다.')
# else:
#     print('윤년이 아닙니다.')

# # 또는

# year = int(input('연도를 입력하세요 : '))
# if year % 4 == 0 :
#     if year % 100 != 0 :
#         print('윤년입니다')
#     elif year % 400 == 0 :
#         print('윤년입니다')
#     else :
#         print('윤년이 아닙니다')
# else :
#     print('윤년이 아닙니다')


