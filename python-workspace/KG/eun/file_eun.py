''''
fil = open('파일 위치', 'w/r/a')
- '파일위치' : \ -> \\ or / (변경)
- w
- r
- wb    : binary(텍스트 아닌 이미지, 동영상 등)
- rb
'''
# write 방법 2가지
writeFile=open('C:\\eun\\python-workspace\\day9\\001.txt', 'w')
# \\001.txt 생성하고 내용 작성 (중복되면 기존 파일 삭제 후 생성)
writeFile.write('str')
writeFile.flush()   # memory에 write 해놓은 값을 file에 저장 후 memory 비움. open은 그대로!!! 이어서 작성 가능~
writeFile.close()

addFile=open('C:\\eun\\python-workspace\\day9\\001.txt', 'a')
# \\001.txt 있으면 내용추가(마지막에 이어적음), 없으면 생성
addFile.write('\nadd str')
addFile.close()

# read 방법 3가지
readFile=open('C:\\eun\\python-workspace\\day9\\001.txt', 'r')
file001 = readFile.read()
print(file001)
readFile.close()

readFile=open('C:\\eun\\python-workspace\\day9\\001.txt', 'r')
line = readFile.readline()  # 한줄씩 읽음  -> str\n
line2 = readFile.readline() #             -> add str
print(line)
print(line2)
readFile.close()

readFile=open('C:\\eun\\python-workspace\\day9\\001.txt', 'r')
lines = readFile.readlines()    # 전체를 한줄씩 list로 저장  -> ['str\n', 'add str']
print(lines)    # list
for i, v in enumerate(lines):   # enumerate: 열거, lines라는 list를 index(0~)와 value로 열거해준다.
    print(i, v)                 #           https://blog.naver.com/dldudcks1779/222772874531?isInf=true
readFile.close()

# 외부편집 txt파일을 python에서 read할때, 한글내용이면 encoding = 'utf-8'을 써야한다.
readFile=open('C:\\eun\\python-workspace\\day9\\002.txt', 'r', encoding= 'utf-8')
while True:
    line = readFile.readline()
    if line == '':
        break
    print(line)
readFile.close()


# file 위치 파악
import os

path = 'c:/eun/python-workspace/day9/'      # 궁금한 폴더 주소
fileName = '003'                            # 궁금한 파일명
path += path + fileName + '.txt'            # 궁금한 파일 주소 완성!

os.path.exists(path)    # True/False return



# quiz -인적사항 등록
name=input('이름 입력 : ')
age=input('나이 입력 : ')
address=input('주소 입력 : ')

writeHong=open('C:\\eun\\python-workspace\\day9/hong.txt', 'w')
writeHong.write(name+'\n'+age+'\n'+address)
writeHong.close()

readHong=open('C:\\eun\\python-workspace\\day9/hong.txt', 'r')
hong = readHong.read()
print(hong)

copyHong=open('C:\\eun\\python-workspace\\day9/hong2.txt', 'w')
copyHong.write(hong)

copyHong.close()
readHong.close()



# quiz -홍파일 내용 수정(홍길동에서 김개똥으로)
readindexHong = open('C:\\eun\\python-workspace\\day9/hong.txt', 'r')
hongs = readindexHong.readlines()   # hongs : list
for index, value in enumerate(hongs):
    print(index, ':', value.rstrip())   # 뒤의 \n 제거

index = int(input('수정할 번호 입력 : '))
newValue = input('수정값 입력 : ')

for i in range(len(hongs)):
    if i == index:
        hongs[i] = newValue+'\n'    # 줄바꿈 그대로 유지하기 위해!

readindexHong.close()

editHong = open('C:\\eun\\python-workspace\\day9/hong.txt', 'w')
print(hongs)
for i in hongs:     # hongs : list, i : str
    editHong.write(i)   # str만 가능
editHong.close()


# quiz -회원가입 프로그램
import os
while True:
    print('='*20)
    print('1.회원가입\n2.회원보기\n3.회원수정\n4.종료')
    option=input('>>> ')

    if option == '1':   # 1. 회원가입 : id로 txt파일 생성 후 파일에 name, age, adr 기록
        id=input('등록할 id 입력 : ')
        writeUser = open(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{id}.txt', 'w')  # user의 id file 생성
        name=input('이름 입력 : ')
        age=input('나이 입력 : ')
        adr=input('주소 입력 : ')
        writeUser.write(name+'\n'+age+'\n'+adr) # 정보 입력
        writeUser.close()
        print('~~~~등록 되었습니다~~~~')

    elif option == '2': # 2. 회원보기 : id입력받아서 해당 txt파일 읽어오기
        id = input('정보 볼 회원 id 입력 : ')
        readUser = open(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{id}.txt', 'r')
        print(readUser.read())
        readUser.close()

    elif option == '3': # 3. 회원수정 : 두 가지 case로 나눔
        print('1. 회원 id 수정\n2. 회원 정보 수정')
        option = input('>>> ')

        if option == '1':   # 1. id수정 : 기존 txt파일의 내용을 새로운 txt파일에 복/붙
            id = input('수정할 회원 id 입력 : ')
            newId = input('새로운 id 입력 : ')
            readUser = open(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{id}.txt', 'r')
            user = readUser.readlines()     # list type
            readUser.close()
            editUserId = open(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{newId}.txt', 'w')
            for i in user:
                editUserId.write(i)
            editUserId.close()
            os.remove(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{id}.txt')    # 이전 id파일 삭제

        elif option == '2': # 2. id그대로, 내용 수정 : id.txt파일을 읽어서 list형태로 수정, 같은 이름의 id.txt파일로 재생성
            id = input('수정할 회원 id 입력 : ')
            readUser = open(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{id}.txt', 'r')
            user = readUser.readlines()     # list type
            for i, v in enumerate(user):
                print(i, ':', v.rstrip())   # value값 뒤의 '\n' 없애기 위해 rstrip 사용
            index = int(input('수정할 항목번호 입력 : '))
            value = input('수정할 새 값 입력 : ')
            for i in range(len(user)):
                if i == index:
                    user[i]=value+'\n'  # '\n'없으면 다음줄과 줄바꿈이 안됨~
            readUser.close()
            editUser = open(f'C:\\eun\\python-workspace\\day9\\quiz_addingID/{id}.txt', 'w')
            for i in user:
                editUser.write(i)
            editUser.close()
        print('수정 완료!!!')

    elif option == '4':
        print('종료합니다~')
        break
   