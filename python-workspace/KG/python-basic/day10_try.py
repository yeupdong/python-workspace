'''
예외처리
- 문제가 발생하면 except로 코드를 작성해준다. 구분없이 작성하면 종속문장을 처리해준다.
에러코드를 작성하면 종속문장이 출력된다.

-예외처리의 장점은 프로그램을 종료시키지 않는다. 
try: 는 문제를 모아놓는다. "문제가 발견되었다."
except: 는 발생한 문제의 처리를 맡는다. "어떻게 해결할 것인가?", 모든 값을 받아주는 except는 항상 맨 아래에 둔다.

try: 에서 문제가 발생하지 않으면 else: 로 넘어간다.

finally: 문제가 발생하든 발생하지 않든 무조건 실행시킨다.

raise : 강제예외를 시킨다. 문법적으로 문제는 안되지만 강제로 예외를 시키는 경우, 예외처리 시 에러코드를 작성하면, 해당 에러코드에 대한 위치를 찾아가 종속문장을 실행시킨다.
'''
# try:
#     n1 = int(input("수 입력 :"))
#     n2 = int(input("수 입력 :"))

#     s = n1/n2
#     print("결과 : ", s)
# except ZeroDivisionError:
#     print("문제 발생")
# except ValueError:
#     print("문제 발생 수 입력")
# print("다음 문장")

# while True:
#     try:
#         num = int(input("수 입력 (종료 0) :")) 
#     except:
#         num = "잘못 입력, 다시..."

#     if num == 0:
#         break
#     print("입력 한 수 :", num)
# print("다음 문장들 실행~~~~~~")

# try:
#     n = int(input("수 :"))
# except:
#     print("except 실행")
# else:
#     print("else 실행")
# print("다음문장실행!!!")

# try:
#     n1 = int(input("수 입력 :"))
#     n2 = int(input("수 입력 :"))
#     s = n1/n2
# except:
#     print("except 실행")
# else:
#     print(f"{n1}/{n2}={s}")
# finally:
#     print("finally 실행")
# print("다음문장실행!!!")

# def test():
#     file = 0
#     try:
#         file = open("c:/aaa1111.txt", "r")
#     except:
#         print("File does not exist.")
#     else:
#         print( file.read() )
#     finally:
#         if file:
#             file.close()
#     print("Continue~~~")

#     try:
#         n = input("Enter num :")
#         if n == "1":
#             return 111
#         elif n == "2":
#             return 222
#     except:
#         pass
#     else:
#         pass
#     finally:
#         print("Run test function")
#         print("This code must be processed.")
#     print("End function test.")
# re = test()
# print("result :", re)

# try:
#     age = int(input("age :"))
#     #print("당신의 나이는 :", age-1)
#     if age < 0:
#         raise Exception("00000000000") #강제로 예외를 발생시킴
# except ValueError:
#     print("Strings not acceptable")
# except Exception as e: #강제예외 출력코드를 "as"와 출력코드 로 받는다.
#     print("No age under 0")
#     print(e)
# except:
#     print("Error!!!!!")
# else:
#     print("Your age is :", age-1)

try:
    min=input("주민번호 앞 자리 입력(예 900402) : ")
    if len(min) != 6:
        raise Exception("잘못 입력")
    if not min.isdigit():
        raise Exception("잘못 입력 숫자 입력하세요")
    elif min[0] > '8':
        raise Exception(min)
except Exception as e:
    print(e,"가입불가")
else:
    print(min,":가입가능")
finally:
    print("프로그램 종료 합니다")



