n1 = 9; n2 =2
print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} * {n2} = {n1*n2}')
print(f'{n1} / {n2} = {n1/n2}')
print(f'{n1} // {n2} = {n1//n2}') #몫을 구해준다.
print(f'{n1} % {n2} = {n1%n2}') #나머지를 구해준다.
print(f'{n1} ** {n2} = {n1**n2}') #제곱을 해준다.
print('\t')
print('\t')
'''
#관계연산자
<,>,<=,>=,==,!=
- 결과적으로 True/False를 판단
- 이항연산자
'''
n1 = 3.1 ; n2 = 3
print('n1 >= n2 :',(n1>=n2)) #T
print('n1 < n2 :',(n1<n2)) #F
print('n1 == n2 :',(n1==n2)) #F
print('n1 != n2 :',(n1!=n2)) #T
print('\t')
print('\t')
#복합대입연산자
num = 10; 
num = num + 100
num += 100
num *= 100
num %= 100
print('\t')
print('\t')
n1 = n2 = 5
n1 += 1; print(n1) #n1 = 6
n1 -= 1; print(n1) #n1 = 5
n1 *= n2; print(n1) #n1 = 25
n1 //= n2; print(n1) #n1 = 5
n1 %= n2; print(n1) #n1 = 0
print('\t')
print('\t')
n1 = 5; n2 = 3
n1 **= n2 #n1 = 125
n1 -= 2 #n1 = 123
print(n1 / 4) #123/4 = 30.75
print(n1 // 4) #123//4 = 30

'''
#논리연산자
여러식을 묶어서 연산한다.
and : 모든 식이 True일 때, 결과는 True이다.
or : 하나라도 True이면, 결과도 True이다.
not : 결과를 반전 시켜준다. 
'''
print(True and True) #T
print(True and False) #F
print(False and True) #F
print(False and False) #F
n1 = 12;
print('n1>10 :', n1>10)
print('n1%2 :', n1%2)
print('0==0 :', 0==0)
print(n1>10 and n1%2==0)
print('\t')
print('\t')
print(True or True) #T
print(True or False) #T
print(False or True) #T
print(False or False) #F
print('not True :', not True)
print('n1>10:', n1>10)
print('not n1>10:', not n1>10)
