#문자열

st = "Have a nice day"

print( st[0])
print( st[1])
print( st[-1])

print( len(st) )

for i in range(len(st)):
    print(st[i], end="")
print("="*20)

print( st[3:6])

st = "Python test. 그리고 programming 할만하다 ^^"
print(st)
print(st.upper()) #대문자로 변경
print(st.lower()) #소문자로 변경
print(st.swapcase()) #상호변경. 대/소문자
print(st.title()) #단어의 첫번째 대문자로 변경

#문제

st = "NevEr-eVer 110gIVe up"
print(st.title()) #
st = st.title() # 변수로 저장을 하고 싶다면 다시 지정을 해서 저장을 해야한다. 그렇지 않으면, 다시 원래대로 돌아간다.
print(st)

st = "Have a nice day"
print(st)
print(st.count('a'))
print(st.count('day'))
print(st.count('dak'))

print(st.startswith("Ha")) #시작문자
print(st.startswith("ha"))

print(st.endswith('day')) #끝문자
print(st.endswith('da'))

#문제

st = "It is a fun Python class"

print(st.count("a"))
print(st.count("s"))

st = "Have a nice day"

print(st)
print(st.find('day'))
print(st.index('day'))
print(st.find('dddd')) #해당값이 존재하지 않을 경우 "-1"로 표시
#print(st.index('dddd')) #해당값이 존재하지 않을 경우 error

num = st.find('a') #변수를 이용해서 해당 인덱스 값을 저장한 한 뒤, 원하는 값을 도풀할 수 있음.
print( st.find('a')) #제일 처음으로 만나는 a의 값을 표현.
print( st.find('a',2)) #인덱스 값을 추가해주면 그 뒤에 있는 a의 인덱스 값을 표현.

print('='*20)

st = 'Have a nice day Have a nice day Have a nice day'
print(st.count('a'))
print('='*20)


st = '  파이썬  '
print(f"*{st}*")
print(f"*{st.strip()}*") #공백을 삭제함. 문자열을 비교할 때 스트립을 가끔 사용하기도 함. 

# name = input("이름 입력 : ")
# print("이름 : ", name)
# if name.strip == "홍길동": #ID를 입력했을 때 혹시라도 추가됐을 공백을 사전방지해준다.
#     print("인증 통과")
# else:
#     print("인증 실패!!!")
    
st = "+++파이썬+++"
print(st)
print( st.strip("+")) #양쪽에 "+"를 제거한다.
print( st.rstrip("+")) #오른쪽에 "+"를 제거한다.
print( st.lstrip("+")) #왼쪽에 "+"를 제거한다.

st = "2015/04/02"
print(st)
print(st.replace("/","."))
print(st.replace(st[0:4], "2022"))

st = """
김개똥-2017년03월24일
홍길동구리-2015년04월02일
선우선녀-2018년05월14일
"""

st = st.replace("-",":")
print(st)

i = 0

for k in range(st.count(':')):
    i = st.find(':',i+1)
    st = st.replace(st[i+1:i+5],'1999')
print(st)

