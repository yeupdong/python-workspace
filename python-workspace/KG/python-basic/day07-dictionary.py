'''
Dictionary
-하나의 값으로 key와 value가 하나의 쌍으로 이뤄져 있다. 
-탐색 속도가 빠르고 사용하기 편리하다.
-중괄호로 묶여 있고, 키와 값의 쌍으로 이뤄져있다.
'''

st = {'stNum':1234, '이름':'홍길동'}
print( st )
print( type(st))

mobile = {"품명":"겔럭시", "가격":1000}
print(mobile)
print(mobile['품명']) #key값을 입력하면 value값이 출력된다.

impo = {}
impo['파이썬'] = 'www.python.org'
impo['네이버'] = 'www.naver.com'
print( impo )
print(impo['파이썬'])
print(impo['네이버'])

# impo = {}
# name = input('등록할 키 입력 : ')
# value = input('등록할 값 입력 : ')
# impo[name] = value
# print(impo)
# print(impo[name])

num = {1:"일", 2:"이", 3:"삼"}
print(num.keys())
print(num.values())

li = list(num.keys())
print(li, li[0])

for i in num.keys():
    print(i,":",num[i])

num = {1:"일", 2:"이", 3:"삼"}
print( num[1] )
print( num.get(1) )

#print( num[111] ) #에러 발생
print( num.get(111) ) #None이라고 뜸.

# key = int(input("key 입력 : "))
# result = num.get(key)
# if result == None:
#     print('찾는 내용이 없습니다')
# else:
#     print(key,":",result)



# while True:
#     menu = {}
#     print("1.메뉴등록\n2.메뉴별 가격 보기\n3.가격 수정\n4.종료")
#     opt = int(input('옵션을 선택하세요. :'))
#     if opt == 1:
#         new_menu = input('메뉴 입력 :')
#         new_price = int(input('가격 입력 :'))
#         for i in range(len(menu)):
#             menu[i] = {new_menu:new_price}
#             i += 1
#     if opt == 2:
#         print(menu)
#     elif opt == 3:
#         edit_menu = input('수정할 목록 입력')
#         edit_price = int(input('수정 가격'))
#     elif opt == 4:
#         print('종료')

#         break
#     else:
#         print('옵션을 다시 선택하세요.')

menu={};  bl = True;  num = 0
while bl:
    print("1.메뉴 등록"); print("2.메뉴별 가격 보기");  print("3.가격 수정");print("4.종료")
    num=int(input(">>> "))
    if num == 1:
        name = input("메뉴 입력 : "); 
        if menu.get(name) != None:  print("등록되어 있습니다!!!")
        else:   menu[name] = input("가격 입력 : ")
    elif num == 2:
        for i in menu.keys():
            print(i,":",menu[i])
    elif num == 3:
        name = input("수정할 목록 입력 : ");
        if menu.get(name) == None:  print("등록 먼저 하세요!!")
        else:    menu[name] = input("수정가격 : ")
    elif num ==4:
        print("프로그램 종료 합니다")
        bl = False


# st = {"학번":1234, "이름":"홍길동"}
# print( st )
# print( st.items() ) #key와 value를 쌍으로 가져온다.

# for k, v in st.items():
#     print(f'{k} : {v}')

# print(st.setdefault("학번",5555))
# print(st)

# print(st.setdefault("학번1",5555)) #해당하는 key가 존재하지 않으면 데이터를 추가시켜준다. 
# print(st)

# ls = [10,{"키":"키에의한 값"},30] #리스트 안에 딕셔너리, 딕셔너리 안에 리스트를 넣을 수 있다.
# print( ls[0] )
# print( ls[1], ls[1]["키"] )
# print( ls[2] )

# dic = {"li":[10,20,30], "k":"value"}
# print( dic["li"], dic["li"][2])
# print( dic["k"])

# info = {}
# info02 = {}
# print('-'*20)
# info02['가수'] = "개가수"
# info02['인원수'] = 3
# info02['노래명'] = "신나리"
# info[info02['가수']] = info02.copy() #copy로 복사를 하면 다른공간에 저장하기때문에 변수값은 영향을 주지 않는다.

# print('-'*20)

# print(info02)
# print(info)

# print('-'*20)

# for k,v in info.items():
#     # print(k)
#     # print(v)
#     for kk,vv in v.items():
#         print(kk,":",vv)

# print('-'*20)

# info02['안녕'] = "하세요"
# print(info)
# print(info02)

# info = {}
# info.clear() #값을 초기화