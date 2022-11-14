#21 문자열 인덱싱
print('{:=^30}'.format('#21'))
#letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
'''
>> letters = 'python'
실행 예
p t
'''
letters = 'python'
print(letters[0], letters[2])

#22 문자열 슬라이싱
print('{:=^30}'.format('#22'))
#자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
'''
>> license_plate = "24가 2210"
'''

st = "24가 2210"
print(st[4:])

#23 문자열 인덱싱
print('{:=^30}'.format('#23'))
# 아래의 문자열에서 '홀' 만 출력하세요.
'''
>> string = "홀짝홀짝홀짝"
실행 예:홀홀홀
'''

string = "홀짝홀짝홀짝"
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i], end='')
print()

print(string[::2]) # [시작인덱스:끝인덱스:오프셋]

#24 문자열 슬라이싱
print('{:=^30}'.format('#24'))
#문자열을 거꾸로 뒤집어 출력하세요.
'''
>> string = "PYTHON"
실행 예:
NOHTYP
'''

st = 'PYTHON'
for i in range(len(st)):
    i+=1
    print(st[0-i], end='')
print()

print(st[::-1])

#25 문자열 치환
print('{:=^30}'.format('#25'))
'''
>> phone_number = "010-1111-2222"
실행 예
010 1111 2222
'''

st = "010-1111-2222"
st1 = (st.replace("-"," "))
print(st1)

#26 문자열 다루기
print('{:=^30}'.format('#26'))
#25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
'''
실행 예
01011112222
'''
st1 = (st.replace("-",""))
print(st1)


#27 문자열 다루기
print('{:=^30}'.format('#27'))
#url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
'''
>> url = "http://sharebook.kr"
실행 예: kr
'''
url = "http://sharebook.kr"
split = (url.split("."))
print(split[1])

#28 문자열은 immutable
print('{:=^30}'.format('#28'))
#아래 코드의 실행 결과를 예상해보세요.
'''
>> lang = 'python'
>> lang[0] = 'p'
>> print(lang)
'''
#error 발생한다. 문자열은 수정할 수 없다. 

#29 replace 메서드
print('{:=^30}'.format('#29'))
#아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
#string = 'abcdfe2a354a32a'

string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#30 replace 메서드
print('{:=^30}'.format('#30'))
#아래 코드의 실행 결과를 예상해보세요.
'''
>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)
'''
#'abcd', string.replace를 새로운 변수에 대입을 시켜주지 않았다.
