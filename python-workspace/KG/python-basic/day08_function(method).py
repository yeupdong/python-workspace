'''
함수(메소드)
- class 안에 함수가 있으면 메소드라고 호칭.
- class 없이 함수만 있으면 함수.
- funcion = 기능 (print, input, sort, find 등등)
- 어떤 기능이 있다면 함수라고 한다.
- 소괄호가 존재하면 95%정도는 함수이다. (=함수 구분방법)

사용방법
def test(args): #전달하는 용도
    종속문장
    return value #return은 생략도 가능
(의미를 부여하는 것이 가장 좋다.)
계속 사용하는 문구 또는 계산식을 다시 작성할 필요없이 가져올 수 있는 장점이 있다.
'''
# def reverseCode():
#     temp = 0
#     result = int(input('수 입력 : '))
#     while True:
#         temp = result % 10
#         result = result // 10
#         print(temp, end=", ")
#         if not result: # 0 = False, 1 = True
#             break
#     print('프로그램 종료')
# if __name__=="__main__": #함수를 다른 페이지에서 호출했을 때 중복 실행이 되는 것을 막기 위해 사용하는 코드. 
# #현재 페이지에서는 주체가 되기때문에 종속문장까지 출력이 되겠지만, 다른 페이지에서 호출된 계산식에서는 실행이 되지 않는다.
#     reverseCode()
# print("종료") 
# #디버깅시 F10은 한줄씩 실행을 시키기때문에 넘어가고, 
# # F11은 단계를 실행시켜주기때문에 함수로 돌아가서 실행이 된다.

# def sumfunc():
#     sum_ = 0    
#     num = int(input("수 입력 : "))
#     for i in range(num+1):
#         sum_ += i
#     print(f'1 ~ {num} 까지의 합 : {sum_}')
# #sumfunc()
# #하나의 함수에 다양한 기능이 있는 경우 = 강한결합. 이렇게 만들지 마세요!! 

# def sumfunc1( num ):
#     sum_ = 0
#     #num = int(input("수 입력 : "))
#     for i in range(num+1):
#         sum_ += i
#     print(f'1 ~ {num} 까지의 합 : {sum_}')

# #num = int(input("수 입력 : ")) #함수 내용은 인지를 하고, 바깥내용을 먼저 실행한다. 
# #sumfunc1( num )

# def sumfunc1( num ):
#     sum_ = 0
#     #num = int(input("수 입력 : "))
#     for i in range(num+1):
#         sum_ += i
#     print(f'1 ~ {num} 까지의 합 : {sum_}')
# num = int(input("수 입력 : ")) #함수 내용은 인지를 하고, 바깥내용을 먼저 실행한다. 
# sumfunc1( num )

# def sumfunc2( num ):
#     sum_ = 0
#     for i in range(num+1):
#         sum_ += i
#     #print(f'1 ~ {num} 까지의 합 : {sum_}')
#     return sum_ #return: 함수를 호출한 곳으로 값을 되돌려 주겠다. 그래서 함수 앞에 변수로 값을 받아준다.
# num = int(input("수 입력 : ")) #함수 내용은 인지를 하고, 바깥내용을 먼저 실행한다. 
# sum_ = sumfunc2( num )
# print(f'1 ~ {num} 까지의 합 : {sum_}')

#연산, 출력, 입력 함수를 각각 만들어 동작
#함수를 어떻게 만들어야하는지 모르겠으면, 동작을 먼저 만든다.

# def input_():
#     num = int(input("수 입력 :"))
#     return num

# def calc_( num ):
#     sum_ = 0
#     for i in range(num+1):
#         sum_ += i
#     return sum_

# def print_(num,sum_):
#     print(f'1 ~ {num} 까지의 합 : {sum_}')

# num = input_()
# sum_ = calc_( num )
# print_( num,sum_)

# def three_(i):
#     if i % 3 == 0:
#         print('i는 3의 배수입니다.')
#     else:
#         print('i는 3의 배수가 아닙니다.')
#         return i
# three_()
# i = int(input('수 입력 : '))

# def primeNum(p):
#     for p in range(1,p+1):
#         if p != 1 and p // p < 2:
#             print('p는 소수입니다.')
#         else:
#             print('p는 소수가 아닙니다.')
#             return p
# primeNum()
# p = int(input('수 입력 : '))

# def reverseNum(r):
#     num = 0
#     while True:
#         num = r % 10
#         r = r // 10
        
#         if not r:
#             break
#         return r
# reverseNum()
# r = int(input('수 입력 : '))
# print(num, end=' ')

# def calculator(num1, num2, res):
#     if opt == 1:
#         print(f'{num1}+{num2}={num1+num2}')
#     elif opt == 2:
#         pass
#     elif opt == 3:
#         pass
#     elif opt == 4:
#         pass 

        
# num1 = int(input('수 입력 : '))
# num2 = int(input('수 입력 : '))
# print('='*20)
# def test( num ):
#     if num % 3 == 0:
#         result = f'{num}. 3의 배수'
#     else:
#         result = f'{num}. 3의 배수 아님'
#     return result

# def myPrint( result ):
#     print( result )

# def myInput():
#     return int(input('수 입력 : '))

# num = myInput()
# result = test(num)
# myPrint(result)

# # return 은 break와 같이 함수를 빠져나가게 하는 성질이 있어서 else를 굳이 안써도 된다. 
# print('='*20)
# def showAvrg(a,b,c):
#     print(f'{a}와 {b}의 평균 : {round(c,1)}')
# def avrg(j,k): #j=2, k=3 변수를 맞출 필요는 없다.
#     return(j+k) / 2
# def display():
#     i = 2; j = 3;
#     f = avrg(i, j)
#     showAvrg(i,j,f)
# display()
# print('다음문장실행')
# #변수 자체가 넘어가는것이 아니라, 변수의 값이 넘어가는 것이다. 


# #함수로 만들기
# year = [ '1999' , '2000' , '2001' ]
# check = 0
# num = input('저장할 년도 입력 : ' )

# for i in year:
#     if num == i:
#         check = 1
#         break
# if check == 1:
#     print( '해당 년도는 존재 합니다. 저장할 수 없음!!!' )
# else:
#     year.append( num )
#     print( num , ' 저장 되었습니다!!!' )

# menu = [ '라면' , '순대' , '김밥' ]
# check = 0
# num = input('등록 메뉴 입력 : ' )
# for i in menu:
#     if num == i:
#         check = 1
#         break
# if check == 1:
#     print( '해당 메뉴는 존재 합니다. 저장할 수 없음!!!' )
# else:
#     menu.append( num )
#     print( num,' 저장 되었습니다!!!' )


