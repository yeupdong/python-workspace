# i = 0
# while i<5:
#     print(i,'종속문장')
#     i+=1
# print('다음문장')

# for i in range(0,5):
#     print(i, '종속문장')
# print('다음문장')

# i = 1
# odd, even = 0,0
# while i <= 10:
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
#     i += 1
# print(f'1~10까지의 짝 합 : {even}')
# print(f'1~10까지의 홀 합 : {odd}')

# i = 1
# odd, even = 0,0
# for i in range(1,11):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(f'1~10까지의 짝 합 : {even}')
# print(f'1~10까지의 홀 합 : {odd}')

# i = 1
# flag = True
# while flag:
#     print(i, '종속문장', end=' ')
#     if i == 5:
#         flag = False
#     i += 1
# print('다음문장실행')

#break: 반복문을 빠져나올 경우 사용
#continue: 반복문 위로 올려보낸다

# =====break=====
# i = 0
# while True:
#     i += 1
#     if i == 3:
#         break
#         print('3')
#     print(i,'출력')
# print('다음문장')


# =====continue=====
# i = 0
# while i <= 5:
#     i += 1
#     if i == 3:
#         continue
#         print('3')
#     print(i,'출력')
# print('다음문장')

#===== while else=====
# i = 0
# while i < 5:
#     i += 1
#     print(i,'종속문장')
# else:
#     print('else실행')
# print('다음문장')


#sum_ = 0
# i = 0
# while True:
#     num = int(input('10~20사이의 숫자를 입력하세요 : '))
#     if num < 10 or num > 20:
#         print('잘못 입력 다시')
#         continue
#     break
# while i <= num:
#         sum_+=i
#         i+=1
# else:
#     print(f'{1}~{num}까지의 합 : {sum_}')

# for i in range(0,3,1):
#     for k in range(0,5,1):
#         if k == 3:
#             break
#         print(f'i : {i}, k : {k}')

# i = 0
# while i < 3:
#     k = 0
#     while k < 5: #while문은 해당 변수를 초기화 하지 않기 때문에 break를 넣어서 맨위로 가져가주어야 한다.
#         if k == 3:
#             break
#         print(f'i : {i}, k : {k}')
#         k += 1
#     i += 1

# cash = int(input('요금을 투입하세요 :'))
# rest = 0
# coffee = 200
# cocoa = 250
# while 0 < cash:
#     print('{:^10}'.format('커피자판기'))
#     print('1. 커피(200)\t 2. 코코아(250)\t 3. 반환\t 4. 종료')
#     option = int(input('메뉴를 선택하세요 : '))
#     if ((option == 1 and cash < 200)) or ((option == 2 and cash < 250)):
#         print('요금이 부족합니다.')
#     elif option == 1:
#         if cash >= rest:
#             cash -= coffee
#             rest = cash
#             print('맛잇게 드세요.')
#     elif option == 2:
#         if cash >= rest:
#             cash -= cocoa
#             rest = cash
#             print('맛있게 드세요.')
#     elif option == 3:
#         print(f'반환금액 : {rest}')
#     elif option == 4:
#         print('종료')
#         break
#     else:
#         print('잘못 선택하셨습니다.')
# else:
#     print('요금이 부족합니다.')

# num = int(input('숫자입력 :'))
# for i in range(1,num):
#     cnt = 0
#     for k in range(1,num+1):
#         if i % k == 0:
#             cnt+=1
#         if cnt == 2:
#             print(i,': 소수')

