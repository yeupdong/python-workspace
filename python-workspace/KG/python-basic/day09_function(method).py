# def sum_func(x1, x2, x3=100): #값을 지정해 놓을 수 있다. default parameter라고 표현
#     re = x1 + x2 + x3
#     return re
# re = sum_func(10,20)
# print('합: ', re)
# re = sum_func(10,20,30) #default값 대신에 넘겨주는 값이 대체한다. 
# print('합: ', re)

#요금 구하는 프로그램 만들기
#환승안함 = a = 500; 환승함 = b *= 2; 장거리 = c = 10000

# def transfer(num = 1, fare = 500):
#     for i in range(1, num+1):
#         fare *= 2
#     return '총 요금은 {}원 입니다.'.format(fare)

# def calc():
#     num = 0
#     opt = int(input("1. No transfer\n2. Transfer\n3. Long distance\n"))
#     if opt == 1:
#         result = transfer()
#     elif opt == 2:
#         num = int(input('number of transfers :'))
#         result = transfer(num)
#     else:
#         result = transfer(fare = 10000)
#     print(result)
# calc()

# #알바 계산기
# #기본근무시간=240시간, 기본시급 12000

# def hourly_rate(hours = 240, rate = 12000):
#     for i in range(1, hours+1):
#         total = hours * rate
#     return f'Total is {total}.'

# def calc():
#     hours = 0
#     opt = int(input("1. standard rate\n2. set hours worked\n3. set rate\n4. set hours worked&rate\n"))
#     if opt == 1:
#         result = hourly_rate()
#     elif opt == 2:
#         hours = int(input("hours you worked :"))
#         result = hourly_rate(hours)
#     elif opt == 3:
#         rate = int(input("set your rate :"))
#         result = hourly_rate(rate)
#     elif opt == 4:
#         hours = int(input("hours you worked :"))
#         rate = int(input("set your rate :"))
#         result = hourly_rate(hours, rate)
#     print(result)
# calc()

# def func01 (*par):
#     print(type(par))
#     for i in par:
#         print(i)
# func01(10,20,30,40)

# print('='*20)




