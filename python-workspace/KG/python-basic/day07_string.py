# st = 'Never ever give up'
# print(st)
# print(st.split()) #특정 문자열을 리스트로 만들어주고, 특정 값을 기준으로 분리를 시킨다.
# print(st.split('e'))


# st = "안녕하세요 오늘 2020/2/23 날씨는 error 춥다"
# sp_li = st.split()
# year = sp_li[2].split('/')

# del( sp_li[4] )
# del( sp_li[2] )
# sp_li.insert(2 , year[0] + "년" + year[1] + "월" + year[2] + "일")
# st = ""
# for i in sp_li:
#     st += i + " "  # print(" ".join(sp_li))로도 표현이 가능.
# print("st => ",st)  

# st = "안녕하세요 반갑습니다"
# print( st )
# print( st.splitlines() ) #엔터값을 기준으로 나눈다. st.split("\n")

# st = '''
# 안녕하세요
# 안녕하세요
# 안녕하세요
# '''
# print( st.splitlines () )

# st = '123'
# test = '%'
# print( test.join(st)) #중간중간에 'test'의 값을 넣어줘라.
# print( '$'.join(st)) #$가 중간중간에 들어간다.

# print( st.join("안녕하세요")) #st값을 "안녕하세요" 중간중간에 들어간다.

# li = ["", "123", "456"] #리스트에도 join함수를 사용할 수 있다.
# print("그래".join(li))

# st = "python"
# print(st)
# print(st.center(10))
# print(st.center(10,"-"))

# print(st.ljust(10))
# print(st.ljust(10,"a"))
# print(st.rjust(10))
# print(st.rjust(10,"a"))
# print(st.zfill(10))

# st = "python te12st 1234"
# print( st.isdigit() ) #숫자로만 구성 #공백이 있으면 문자로 인식이 되기 때문에 False
# print( st[9:11].isdigit() )

# print( st.isalpha() ) #영어로 구성 #공백이 있으면 문자로 인식이 되기 때문에 False
# print( st[:6].isalpha() ) 

# print( st.isalnum() ) #알파벳+숫자로만 구성 #공백이 있으면 문자로 인식이 되기 때문에 False
# print( st[7:13].isalnum() )

# print( st.islower() ) #소문자
# print( st.isupper() ) #대문자
# print( st.isspace() ) #공백

#문제
accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
replaceAB = accountBook.split(',')#,기준으로 리스트로 저장
k=0
for i in replaceAB:
    replaceAB[k]=i.lstrip() #각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
    k+=1
kk='$ '
print('item'.ljust(10),end='')
print('date'.ljust(10),end='')
print('$(price)'.ljust(10))
for i in range(len(replaceAB)):
    z=replaceAB[i].split() #공백을 기준으로 리스트로 저장
    for k in range(len(z)):
        if k == 0 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k ==1 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k == 2 : 
            print("{:,}".format(int(z[k])).join(kk).ljust(10)) 

info = """
jo 91bc08-3022023
cho 900402-1011232
test 1234567-1234567
lee 980908-3a2b0c3
kim 900514-2022023
"""

print( info )
print(info.count('-'))
k=0
for i in range( info.count('-') ):
    k=info.find('-' , k+1)
    if info[k+1:k+8].isdigit() and \
                not info[k-7:k].isdigit() and \
                            info[k-6:k].isdigit():
        info = info.replace(info[k+1:k+8] , '*******' )
print( info )

