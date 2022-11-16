#입력, 연산, 출력 함수를 만들고 수(num)를 입력했을 때, 짝수만 리스트에 넣어서 결과 값을 내는 함수를 만드시오.
#함수 예) input_, even_list, print_list
#힌트 for문, append

# def input_():
#     return int(input('수 입력 :'))

# def even_list(num):
#     result = []
#     for i in range(1,num+1):
#         if i % 2 == 0:
#             result.append(i)
#     return result

# def print_list(ls):
#     print(ls)

# num = input_()
# ls = even_list(num)
# print_list(ls)


# 주어진 횟수만큼 연산을 반복하는 계산기 제작

# <입력받을 것>
# 첫번째 수 입력            : num
# 반복할 수 입력            : repeatNum
# 반복할 횟수 입력          : cnt
# 연산자(+,-,*,/) 입력      : oper

# <제작할 함수>
# 연산자에 따라 계산하는 함수
# 계산함수를 cnt만큼 반복하는 함수

# <출력 예시>
'''
첫번째 수 입력 : 5
반복할 수 입력 : 1
반복할 횟수 입력 : 3
연산자(+,-,*,/) 입력 : -
5에서 1을 3번 -한 값은 2입니다.
'''

# def input_():
#     num1 = int(input('첫번째 수 입력 :'))
#     num2 = int(input('두번째 수 입력 :'))
#     cnt = int(input('반복할 횟수 입력 :'))
#     oper = input('연산자 입력 :')
#     return num1, num2, cnt, oper

# num1 = int(input('첫번째 수 입력 :'))
# f_num = num1
# num2 = int(input('두번째 수 입력 :'))
# cnt = int(input('반복할 횟수 입력 :'))
# oper = input('연산자 입력 :') 

# def calc():
#     global num1, num2
#     for i in range(cnt):
#         if oper == "+":
#             num1 += num2
#         elif oper == "-":
#             num1 -= num2
#         elif oper == "*":
#             num1 *= num2
#         elif oper == "/":
#             num1 /= num2
#     return num1
# num_ = calc()
# print("{}과{}를 {}번 {}한 결과 값은 {}입니다.".format(f_num,num2,cnt,oper,num_))
  
#함수를 활용해서 도시의 이름을 사용자 입력 프로그램 
# 1 도시이름 입력 칸 2 종료 
# 이외의 숫자 입력 불가

def menu_():
    print('1. 도시추가\t2.종료')
    return int(input('옵션을 선택해주세요 : '))

def input_(cities):
    ls = []
    cities = input("도시를 영어로 입력하세요")
    ls.append(cities)
    return cities

def cities_list(ls):
    while True:
        select = menu_
        if select == 1:
            input_(ls)
        if select == 2:
            break
        else:
            print('잘못 입력 하셨습니다.')
        print('종료')    
cities = []
cities_list(cities)
            



list_data=[]
def input_user(list_1):
    list_1= input("도시를 영어로 입력하세요")
    list_data.append(list_1[:3])
    return list_1

def select_manu() :
    print('1. 도시추가 2. 종료')
    return int(input('값을 입력하세요'))

def main(list_data):
    while True :
        selct = select_manu()
        if selct ==1 :
            input_user(list_data) 
        elif selct ==2:
            break
        else :
            print('올바른 값을 입력해주세요')
        print('종료')
cities = []
main(cities)   