'''
사용 모드
- w : 파일에 내용 출력
- a (append) : 파일이 없으면 새로 만들어서 저장하고, 이미 존재하는 파일에는 이어쓰기
- r (read) : 파일에 내용 가져오기
- wb : 텍스트가 아닌 이미지, 동영상 등
       바이너리로 처리되는 값 출력
- rb : 읽어오기
file.close는 무조건 포함시켜줘야 스트림이 닫히고 출력이 된다.
'''

# file = open("D:/0. k-digital python/test.txt","w")
# st = input("출력할 내용 입력 : ")
# file.write(st)
# file.close

# file = open("D:/0. k-digital python/test.txt","r")
# st = file.read()
# file.close()
# print("파일에서 얻어온 값 : ", st)

#문제 
# 파일을 만들고 내용 입력하기

# name = input("이름 입력 :")
# age = input("나이 입력 :")
# address = input("주소 입력 :")
# file = open("D:/0. k-digital python/personal info.txt","w")

# file.write(name+"\n")
# file.write(age+"\n")
# file.write(address)

# file.close()

# #파일 저장내용 가져오기
# write_file = open("D:/0. k-digital python/personal info_1.txt","w")
# read_file = open("D:/0. k-digital python/personal info.txt","r")

# #print( read_file.read() )
# write_file.write( read_file.read() )
# write_file.flush() #해당 내용을 지워버림.
# write_file.close()
# read_file.close()

# read_file = open("D:/0. k-digital python/abcd.txt","r", encoding="utf-8")
# print(read_file.read())

#encoding, decoding = 어떠한 방식으로 문자를 번역할것인가? 한글은 utf-8 으로 처리하는 것이 좋다.

read_file = open("D:/0. k-digital python/personal info.txt","r")
# st = read_file.read()
# print(st)
# print(type(st))
'''
s1 = read_file.readline()
s2 = read_file.readline()
s3 = read_file.readline()
s4 = read_file.readline()
print(s1)
print(s2)
print(s3)
print(s4)

if s4 == "":
    print("더 이상 데이터 없음")
'''

# while True:
#     s = read_file.readline()
#     if s == "":
#         print("데이터 없음!!!")
#         read_file.close()
#         break
#     print(s, type(s))

# read_file = open("D:/0. k-digital python/personal info.txt","r")

# s = read_file.readlines()
# print("---lines---")
# print(s ,type(s))
# read_file.close()

print('-'*20)

# read_file = open("D:/0. k-digital python/personal info.txt","r", encoding="utf-8")
# s = read_file.readlines()
# for i in range(len(s)):
#     #print(f'{i}:{s[i]}')
#     opt = int(input("수정할 번호 입력 :"))
#     if opt == i:
#         s[i] = input("수정값 입력 :")
#         break
#     else:
#         print("옵션을 다시 선택하세요.")
# read_file.close()


# print('-'*20)

# read_file = open("D:/0. k-digital python/personal info.txt","r", encoding="utf-8")

# s = read_file.readlines()
# for i, v in enumerate(s):
#     print(f'{i}.{v}')
# num = int(input('수정할 번호 입력 :'))
# value = input('수정할 값 입력:')

# if len(s)-1 == num:
#     s[num] = value
# else:
#     s[num] = value+"\n"
# read_file.close()

# write_file = open("D:/0. k-digital python/personal info.txt","w")
# for i in s:
#     write_file.write(i)
# write_file.close()

# path = "D:\0. k-digital python"
# import os
# fileName = input("파일명 입력 :")
# path += fileName+".txt"
# print("path : ", path)
# print( os.path.exists(path))

# if os.path.exists(path):
#     file = open( path, "r")
#     print("----파일읽기----")
#     print( file.read())
#     file.close()


#회원가입 프로그램 만들기
import os

while True:
    print("{:=^30}".format("회원가입 프로그램"))
    opt = int(input("1. 회원가입\n2. 회원보기\n3. 회원수정\n4. 종료\n>>>"))
    if opt == 1:
        path = "D:/0. k-digital python/"
        import os
        fileName = input("파일명 입력 :")
        path += fileName+".txt"
        if os.path.exists(path):
            print("이미 등록된 회원입니다. 2번을 눌러 회원정보를 조회하세요.")
        else:
            member_name = input("이름 입력 :")
            member_age = input("나이 입력 :")
            member_address = input("주소 입력 :")
            write_file = open(path,"w")
            write_file.write(member_name+"\n")
            write_file.write(member_age+"\n")
            write_file.write(member_address)
            write_file.close()
            print("회원가입이 완료되었습니다.")
    elif opt == 2:
        path = "D:/0. k-digital python/"
        fileName = input("파일명 입력 :")
        path += fileName+".txt"
        if os.path.exists(path):
            read_file = open( path, "r")
            print(f"----{fileName}----")
            print( read_file.read())
            read_file.close()
        else:
            print("파일명을 다시 입력해주세요.")
    elif opt == 3:
        path = "D:/0. k-digital python/"
        fileName = input("파일명 입력 :")
        path += fileName+".txt"
        if os.path.exists(path):
            edit_file = open( path, "r")
            edit_file = edit_file.readlines()
            print(edit_file)
            
            for i in range(len(edit_file)):
                print(f'{i}:{edit_file[i]}')
            while True:
                edit = int(input("수정할 번호 입력 :"))
                if edit == 0 or edit == 1 or edit == 2:
                    break
                else:
                    print("옵다선")
            edit_file[edit] = input("수정정보 입력 :")+"\n"
            write_file = open( path, "w")
            for i in edit_file:
                write_file.write(i)
            write_file.close()
    elif opt == 4:
        print("프로그램 종료")
        break
    else:
        print("옵션을 다시 선택해주세요.")
