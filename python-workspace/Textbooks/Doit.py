# '''
# head = 'python'
# tail = ' is fun!'
# print(head + tail)
# a = 'python'
# print(a*2)

# #문자열 포멧

# print('Error is %d percent' %98) #%d는 integer를 대입
# print('Error is %d%%' %98)
# print('I eat %s appels.' %'five') #%s는 문자열을 대입
# number = 3
# print('I eat %d apples.' %number) #변수도 대입 가능
# number = 10
# day = 'three'
# print('I ate %d apples. So I was sick for %s days.' %(number,day)) #여러 값을 한번에 대입

# #문자열 포멧으로 정렬하기

# print('%10s' %'hi') #%와 s포멧문자 사이의 숫자는 공백을 의미한다. 8공백이 생기고 나머지 2자리는 hi로 채워진다.
# print('%-10sjane' %'hi') #hi를 왼쪽에 정렬시킨뒤 8개의 공백이 채워졌다.

# #문자열 포멧으로 소수점 표현하기

# print('%0.4f' %0.12345678) #소수점 4자리 까지만 나오는 것을 확인할 수 있다.
# print('%10.4f' %0.123456) #우로 정렬한 뒤 숫자를 제외하여 4개의 공백이 생겼다.

# #format함수

# print('I eat {0} apples.'.format(3)) #()안에 있는 인덱스 번호를 입력한다. 이 때 ()안에는 숫자, 문자, 변수 상관없다.
# print('{0:<10}'.format('hi')) #왼쪽정렬
# print('{0:>10}'.format('hi')) #오른쪽정렬
# print('{0:^10}'.format('hi')) #가운데정렬
# print('{0:=^10}'.format('hi')) #공백을 채우려면 콜론과 방향 사이에 채울값을 넣는다.
# print('{0:0.4f}'.format(0.12345)) #소수점자릿수 표현
# '''
# #f문자열 포멧팅
# name = '이름'
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}세 입니다.')
# print(f'나는 내년이면 {age+1}살이 된다.')
# d = {'name':'이름', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]} 입니다.')
# print(f'{"hi":<10}')
# print(f'{"hi":>10}')
# print(f'{"hi":^10}')
# print(f'{"hi":=^10}')
# print(f'{0.123456:0.4f}')
# print(f'{"python":!^12}')

#while and for questions

#Q1
# a = 'life is too short, you need python'
# if 'wife' in a and 'you' not in a: #none
#     print('python')
# elif 'python' in a and 'you' not in a: #none
#     print('python')
# elif 'shirt' not in a: #shirt
#     print('shirt')
# elif 'need' in a: 
#     print('need')
# else:
#     print('none')

#Q2
# sum_ = 0
# i = 1
# while i < 1001:
#     if i % 3 == 0:
#         sum_ += i
#     i += 1
# print(sum_)

#Q3
# i = 0
# while True:
#     i += 1
#     if i > 5:
#         break
#     print('*'*i)

#Q4
# for i in range(1,101):
#     print(i,end='\t')
#     if i % 10 == 0:
#         print()

#Q5
# sum_ = 0
# a = [70,60,55,75,95,90,80,80,85,100]
# for i in a:
#     sum_ += i
# print(sum_)
# avg = sum_/10
# print(avg)