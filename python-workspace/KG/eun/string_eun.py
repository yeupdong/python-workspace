'''
문자열
'''

st='Have a nice day'
st[0]   # H
st[1]   # a
st[0:4] # Hav
st[-1]  # y
len(st) # 15 (공백포함)

for i in st:
    print(i, end='')    # Have a nice day

'''
string 변형 (저장 X)
- st.upper()        : 대문자로
- st.lower()        : 소문자로
- st.swapcase()     : 대<->소 문자
- st.title()        : 단어(특수문자, 숫자, 공백 기준) 앞글자만 대문자, 나머지는 소문자로
'''

'''
string methods (아래 링크 ctrl+click)
https://www.w3schools.com/python/python_strings_methods.asp
<< 배운 내용 정리 >>
- st.count(str)         : int
- st.startswith(str)    : True/False
- st.endswith(str)      : True/False
- st.find(str)          : index (첫번째 하나만 찾음)
- st.find(str, index+1) : index (두번째도 찾음)
- st.strip()            : 양쪽 공백 제거
- st.rstrip()
- st.lstrip()
- st.replace(oldValue, newValue)    : oldValue -> newValue
- st.replace(st[index:index+n], newValue)   : index ~ (index+n)까지의 값 -> newValue
- st.split()            : 공백 기준 분리 (default : 공백)
- st.split('/')         : / 기준 분리
- st.splitlines()       : 줄바꿈 기준 분리
- ' '.join(st)          : st 한글자 사이마다 ' '(공백) 추가
- st.center(10)         : 10칸 확보, 가운데 정렬
- st.ljust(10)          :          , 왼쪽 정렬
- st.rjust(10)          :          , 오른쪽 정렬
- st.zfill(10)          :          , 오른쪽 정렬 (빈칸 zero로 채움)
- st.isdigit()          : 숫자?         -> True/False
- st.isalpha()          : 영어?         -> True/False
- st.isalnum()          : (영어+숫자)?  -> True/False
- st.islower()          : 소문자?       -> True/False
- st.isupper()          : 대문자?       -> True/False
- st.isspace()          : 공백?         -> True/False



- del(ls[index])        : list의 index번째 값을 delete
- ls.insert(index, newValue)    : list의 index번째에 newValue 추가

'''
st.count('a')   # 3 (int)
st.startswith('ha')     # True/False
st.endswith('ay')       # True/False


