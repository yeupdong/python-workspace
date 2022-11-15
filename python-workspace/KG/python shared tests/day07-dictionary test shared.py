#성진이는 얼마전 수영강습을 등록했다. 그리고 해당 스포츠센터의 락커룸과 신발장을 배정 받았다.
#스포츠센터에서는 혼동을 줄이기 위해 락커룸과 신발장의 번호는 항상 동일하게 배정해준다.
#어느날 변덕쟁이인 성진이는 등록된 락커룸의 번호가 마음에 안들어서 옮기고 싶다고 했다.
#스포츠센터는 성진이의 락커룸과 신발장을 옮겨주었다.
#스포츠센터의 락커룸과 신발장번호를 등록 및 변경하고 현황을 보여주는 프로그램을 작성해보자. 
#단, 락커룸 변경시, 기존에 사용하던 락커룸의 번호는 프로그램에서 제외시켜주어야 한다. (힌트: del을 이용)

#예시
'''
========락커룸/신발장 현황 관리자========
1.락커룸 등록
2.등록된 락커룸과 신발장 현황
3.락커/신발장 번호 변경
4.종료
옵션을 선택하세요. :
'''
'''
========락커룸/신발장 현황 관리자========
1.락커룸 등록
2.등록된 락커룸과 신발장 현황
3.락커/신발장 번호 변경      
4.종료
옵션을 선택하세요. : 1       
락커룸 번호 입력 : 1
신발장 번호 입력 : 1
락커룸과 신발장 등록이 완료되었습니다. 
'''
'''
========락커룸/신발장 현황 관리자========
1.락커룸 등록
2.등록된 락커룸과 신발장 현황
3.락커/신발장 번호 변경
4.종료
옵션을 선택하세요. : 2
락커룸 번호 : 1, 신발장 번호 : 1
락커룸 번호 : 2, 신발장 번호 : 2
락커룸 번호 : 3, 신발장 번호 : 3
'''
'''
========락커룸/신발장 현황 관리자========
1.락커룸 등록
2.등록된 락커룸과 신발장 현황
3.락커/신발장 번호 변경
4.종료
옵션을 선택하세요. : 3
현재 락커룸 번호 입력 : 1
옮기고 싶은 락커룸 번호 입력 : 4
자리를 옮길 신발장 번호 입력 : 4
'''
'''
========락커룸/신발장 현황 관리자========
1.락커룸 등록
2.등록된 락커룸과 신발장 현황
3.락커/신발장 번호 변경
4.종료
옵션을 선택하세요. : 2
락커룸 번호 : 2, 신발장 번호 : 2
락커룸 번호 : 3, 신발장 번호 : 3
락커룸 번호 : 4, 신발장 번호 : 4
'''
'''
========락커룸/신발장 현황 관리자========
1.락커룸 등록
2.등록된 락커룸과 신발장 현황
3.락커/신발장 번호 변경
4.종료
옵션을 선택하세요. : 4
이용해주셔서 감사합니다.
'''

# member={}  
# opt = 0
# lock_num = 0
# while True:
#     print('{:=^30}'.format('락커룸/신발장 현황 관리자'))
#     print("1.락커룸 등록")
#     print("2.등록된 락커룸과 신발장 현황")  
#     print("3.락커/신발장 번호 변경")
#     print("4.종료")
#     opt=int(input("옵션을 선택하세요. : "))
#     if opt == 1:
#         lock_num = int(input("락커룸 번호 입력 : ")) 
#         if member.get(lock_num) != None:  
#             print("해당 락커는 이미 등록되어 있습니다.")
#         else:   
#             member[lock_num] = int(input("신발장 번호 입력 : "))
#             print('락커룸과 신발장 등록이 완료되었습니다.')
#     elif opt == 2:
#         for i in member.keys():
#             print('락커룸 번호 : {}, 신발장 번호 : {}'.format(i,member[i]))
#         if lock_num == 0:
#             print("락커를 먼저 등록해주시기 바랍니다.")
#     elif opt == 3:
#         lock_num = int(input("현재 락커룸 번호 입력 : "))
#         if member.get(lock_num) == None:  
#             print("락커를 먼저 등록해주시기 바랍니다.")
#         else:
#             lock_num2 = int(input("옮기고 싶은 락커룸 번호 입력 : "))
#             del member[lock_num]
#             member[lock_num2] = int(input("자리를 옮길 신발장 번호 입력 : "))
#     elif opt == 4:
#         print("이용해주셔서 감사합니다.")
#         break


'''
컴퓨터 관리자로 로그인하기 5회 실패시 계정잠깁니다 출력하기.
ex)
관리자 아이디를 입력하세요: admin
관리자 비밀번호를 입력하세요: 12345
관리자 계정으로 로그인에 성공하셨습니다.
.
.
.
관리자 아이디를 입력하세요: admin
관리자 비밀번호를 입력하세요: 1414
아이디 또는 비밀번호를 잘못 입력하셨습니다.
5회 틀릴 시 계정이잠깁니다. 4회째 시도중
'''

manager = {}
admin = input('관리자 아이디를 입력하세요: ')
pw = int(input('관리자 비밀번호를 입력하세요: '))
cnt = 0
while True:
    print('{:^30}'.format('컴퓨터 관리자'))
    admin = input('관리자 아이디를 입력하세요: ')
    pw = int(input('관리자 비밀번호를 입력하세요: '))
    cnt += 1
    if manager.get[admin] == None:
        print('아이디 또는 비밀번호를 잘못 입력하셨습니다.')
    if manager.keys() != None:
        





'''
사용자 입력을 통해서 딕셔너리로 구성된 리스트를 만드는 프로그램을 만들어보자

조건
- 딕셔너리의 개수, 딕셔너리의 요소 수는 자유롭게 추가 가능
- 단 딕셔너리의 키는 반드시 숫자형, 밸류는 반드시 문자열만 가능 
'''