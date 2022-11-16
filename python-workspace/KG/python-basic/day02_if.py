'''
#제어문
- 프로그램의 흐름을 제어한다.
- if, for, while, break, continue

#if문
if 조건식: #True이면 종속문장으로 넘어가고, False이면 다음문장으로 넘어간다.
    종속문장
다음문장
'''

#example
print('1.쉬운게임')
print('2.어려운게임')
print('3.종료')
num = int(input('>>>>:'))
if num == 1:
    print('쉬운게임 실행')
if num == 2:
    print('어려운 게임 실행')
if num == 3:
    print('게임 종료')


n1 = 5; n2 = 10
if n1 > n2:
    print('n1이 n2보다 크다.')


n1 = int(input('수 입력:'))
if n1 % 2 == 0:
    print(f'{n1}은 짝수입니다.')
    print('종속문장 실행')
print('다음문장실행')
print('다음문장실행')


#절대값 구하기
num = int(input('정수를 입력하세요. :'))
if num > 0:
    print('절대값 :', num)
if num < 0:
    print('절대값 :', -num)
print('끝')


#가장 큰 수 구하기
a = int(input('첫번째 숫자'))
b = int(input('두번째 숫자'))
c = int(input('세번째 숫자'))
if a > b and a > c:
    print(f'가장 큰 수는 {a} 입니다.')
if b > a and b > c:
    print(f'가장 큰 수는 {b} 입니다.')
if c > a and c > b:
    print(f'가장 큰 수는 {c} 입니다.')

'''
#if, else
if 조건식:
    종속문장
else:
    종속문장
다음문장들 실행
'''

n = int(input('수 입력'))
if n%2 == 0:
    print('짝수')
else:
    print('홀수')
print('다음문장들 실행')


n1 = -1
if n1>0:
    print('n1은 0보다 크다.')
    if n1%2 == 0:
        print('n1은 양의 짝수 입니다.')
    else:
        print('n1은 양의 홀수 입니다.')
else:
    print('n1은 음수입니다.')


n1 = 'aaa'; n2 = 'aaa'
if n1 == n2:
    print('같다')
else:
    print('다르다')


id_1 = str(input('저장할 ID입력 :'))
pw_1 = str(input('저장할 PW입력 :'))
print('인증 프로그램 입니다.')
print('ID와 PW를 입력하세요.')
id_2 = str(input('ID입력 :'))
pw_2 = str(input('PW입력 :'))
if id_1 == id_2:
    if pw_1 == pw_2:
        print('인증통과')
    else:
        print('비밀번호가 틀렸습니다.')
else:
    print('등록되지 않은 아이디 입니다.')

'''
#elif
if 조건식: #True면 종속문장 실행. False면 elif로 감.
    종속문장
elif 조건식: #True면 종속문장 실행. False면 다음 elif로 감.
    종속문장
elif 조건식: #True면 종속문장 실행. False면 True가 없기때문에 else로 감.
    종속문장
else:
    종속문장
다음문장
'''
num = int(input('수 입력: '))
if num > 100:
    print('100보다 크다')
elif num > 90:
    print('90보다 크다')
elif num > 80:
    print('80보다 크다')
elif num > 70:
    print('70보다 크다')
else:
    print('그 외의 값')
print('다음 문장들 실행')

