# 1-1).입력한 데이터가 3의 배수인 경우 출력 하시오.

'''
num = int(input('수 입력 :'))
for i in range(1,num):
    if i % 3 == 0:
        print(i)
'''

# 1-2).수를 입력 받아 짝,홀수를 구분하여 출력 하시오.

'''
num = int(input('수 입력 :'))
for i in range(1,num):
    if i % 2 == 0:
        print(f'{i}는 짝수다.')
    else:
        print(f'{i}는 홀수다')
'''

# 1-3).두수를 입력 받아 큰 수를 출력 하시오.

'''
num1 = int(input('수 입력 :'))
num2 = int(input('수 입력 :'))
while True:
    max_ = 0
    min_ = 0
    if num1 > num2:
        max_ = num1
        min_ = num2
    elif num2 > num1:
        max_ = num2
        min_ = num1
    print(max_)
    break
'''

# 1-4).수를 입력받아 절대값을 구하는 프로그램을 작성 하시오.

'''
num = int(input('정수를 입력하세요. :'))
if num > 0:
    print('절대값 :', num)
if num < 0:
    print('절대값 :', -num)
print('종료')
'''

# 2-1).날짜를 입력 받아 요일을 구하시오.
# 단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일
# 어떤 값을 입력 받던 요일이 정확히 출력 되게 만드시오.

'''
num = int(input('수 입력 :'))

for i in range(1,num+1):
    if i % 7 == 0:
        print(f'{i}일은 일요일이다.')
    if i % 7 == 1:
        print(f'{i}일은 월요일이다.')
    if i % 7 == 2:
        print(f'{i}일은 화요일이다.')
    if i % 7 == 3:
        print(f'{i}일은 수요일이다.')
    if i % 7 == 4:
        print(f'{i}일은 목요일이다.')
    if i % 7 == 5:
        print(f'{i}일은 금요일이다.')
    if i % 7 == 6:
        print(f'{i}일은 토요일이다.')
'''

# 2-2).세수를 입력 받아 큰 수를 출력 하시오.

'''
num1 = int(input('수 입력 :'))
num2 = int(input('수 입력 :'))
num3 = int(input('수 입력 :'))

if num1 > num2 and num1 > num3: 
    max_ = num1
elif num2 > num1 and num2 > num3:
    max_ = num2
elif num3 > num1 and num3 > num2:
    max_ = num3
print(max_)
'''

# 2-3).두수를 입력 받아 큰 수가 짝수이면 출력 하시오.

'''
num1 = int(input('수 입력 :'))
num2 = int(input('수 입력 :'))
max_ = 0
while True:
    if num1 > num2:
        max_ = num1
    if num2 > num1:
        max_ = num2
    if max_ % 2 == 0:
        print(f'큰 수는 {max_}입니다.')
    break
'''

# 2-4).두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력 하시오.

'''
num1 = int(input('수 입력 :'))
num2 = int(input('수 입력 :'))
sum_ = num1 + num2
while True:
    if sum_ % 2 == 0 and sum_ % 3 == 0:
        print(f'{num1}와 {num2}의 합은{sum_} 이고, 짝수이며 3의 배수이다.')
    break
'''

# 3-1).1~100 까지의 총 합을 구한다. 단, 3의 배수는 제외하고 3의 배수이며 5의 배수는 제외하지 않는 조건이다.

'''
sum_ = 0
sum_2 = 0
for i in range(1,101):
    if i % 3 != 0:
        sum_ += i
print(f'3의 배수가 아닌 수들의 합{sum_}')

for k in range(1,101):
    if k % 15 == 0:
        sum_2 += k
print(f'3의 배수이며, 5의 배수인 수{sum_2}')

print(f'1~100사이의 수에서 3의 배수를 제외하고 5의배수는 제외하지 않은 값들의 합은 {sum_+sum_2}이다.')
'''

# 3-2).두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오
# 1입력, 10입력 => 55
# 10입력,1입력 => 55

'''
num1 = int(input("수 입력 :"))
num2 = int(input("수 입력 :"))
sum_ = 0

for i in range(num1,num2+1):
        sum_ += i
for i in range(num2,num1+1):
        sum_ += i
print(sum_)
'''

# 3-3).첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 이 되는 날 입금해야 하는 금액은 얼마인지 구하시오
# (첫날 10, 둘 째날 20 , 셋 째날 40 . . .무조건 2배씩 증가되는 값이다)

'''
money=10
for i in range(2, 31):
    money *= 2
print('30째날 입금할 금액은 {:,}원입니다.'.format(money))
'''

day=0
money = 10
while day < 30:
    day += 1
    if day == 1:
        money = 10
    else:
        money *= 2
print(money)


firstday = 10
count=0
while count<30:
    count+=1
    if count==1:
        firstday=10
    else:
        firstday *=2
print("{}째날, {:,}원".format(count,firstday))

# 3-4) 아래와 같이 출력되게 2중 for문을 이용하여 출력하시오
# 상위포문 0 일 때 하위 포문 : 0 0 0 0 0
# 상위포문 1 일 때 하위 포문 : 0 1 2 3 4
# 상위포문 2 일 때 하위 포문 : 0 2 4 6 8
# 상위포문 3 일 때 하위 포문 : 0 3 6 9 12
# 상위포문 4 일 때 하위 포문 : 0 4 8 12 16

'''
for i in range(0,5):
    print(f'상위 포문 {i} 일때 하위 포문 :', end=' ')
    for k in range(0,5):
        print(f'{i*k}', end=' ')
    print()
'''

# 4. 랜덤과 set을 이용하여 로또 프로그램을 만드시오

'''
import random

s = set()
for i in range(6):
    num = random.randrange(1,45)
    s.add(num)
print(s)
'''

# 5. 다음 내용을 lambda와 map을 이용하여 아래와 같이 표현하시오
# day = { '날짜' : ['2018.01.01.','2019.02.02','2020.03.03'] }
# 2018년 01월 01일
# 2019년 02월 02일
# 2020년 03월 03일

'''
day = {'날짜':['2018.01.01','2019.02.02','2020.03.03']}

ls = list(map(lambda x : x.split('.'), day['날짜']) )
for i in ls:
    print(f'{i[0]}년 {i[1]}월 {i[2]}일')
'''