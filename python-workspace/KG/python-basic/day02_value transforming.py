flt = 123.123
print(flt + 100)
st1, st2 = '파','이썬'
print(st1+st2)
#숫자끼리, 문자끼리 연산이 가능하다. 그러나 숫자와 문자를 함께 연산할 수 없다.

num = 100
print(type(num))
num = '100'
print(type(num))
num = 123.123
print(type(num))

'''
int = integer (정수값)
float = floating point number (실수값)
str = string(문자값)

int() = int값으로 변환
float() = float값으로 변환
str = str값으로 변환
'''
print('\t')
print('\t')
#문제
su = 100
num = '100'
flt = '1.111'
print(su + int(num))
print(su+float(flt))
print(str(su)+num)