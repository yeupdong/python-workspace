"""
error발생해도 programming이 계속 될 수 있도록!
"""
try:
    print('에러 발생 코드')           # error발생 -> except ~~

    # raise -> except 로 넘어감! 강제로 예외 발생 시키는 문법!
    if '조건문 1':
        raise ValueError            # True -> 강제로 예외 발생 -> ValueError 이동

    elif '조건문 2':
        raise Exception('value')    # True -> 강제로 예외 발생 -> Exception 이동, value 전달

except ValueError:
    print('값 에러 발생')

except Exception as e:              # 위의 value를 e라는 변수로 받음.
    print('특정 에러 발생')
    print(e)

except:                             # 나머지 모든 error 경우 (가장 아래 위치해야함)
    print('나머지 에러 발생')

else:
    print('에러 발생 안했을때 실행되는 코드')

finally:
    print('error 여부 상관없이 항상 실행되는 코드')

print('다음 코드')



## ex 1 )
try:
    n1=int(input('수 입력 : '))    # 수가 아닌 값 입력 --> 1 이동
    n2=int(input("수 입력 : "))
    s=n1/n2                        # n2 == 0 인 경우 --> 2 이동

except ValueError:          # Error 1
    print('숫자 입력하세요.')
except ZeroDivisionError:   # Error 2
    print('0으로 나눌 수 없습니다.')
except:                     # Error
    print('에러 발생!')

else:                       # 에러 없음
    print('나누기 성공~')
    print('결과 :', s)

finally:                    # 항상 실행
    print('프로그램 종료~!')


## ex 2 ) while loop 반복문에서의 try
while True:
    try:
        num = int(input('수 입력(종료:0) : '))

    except:
        print('error 발생! 다시 입력하세요.')
        continue    # continue 사용 안할때는 아래 3줄을 else: 로 처리
    
    if num == 0:
        break
    print(num)


## ex 3 ) file.txt 존재 유무 판단!
try:
    file=input('파일 이름 입력 : ')
    readFile=open(f'c:/eun/python-workspace/day9/{file}.txt', 'r')
    print(readFile.read())
    
except FileNotFoundError:
    print('파일이 존재하지 않음')
except UnicodeDecodeError:
    print('한글로 작성된 파일입니다')
except:
    print('다른 에러 발생!')

else:   # 파일 존재
    print(readFile.read())
    readFile.close()

finally:
    print(f'{file}.txt 존재 유무 판단 완료!')


## ex 4 ) 함수 안의 try (짝/홀 판단 함수)
def EvenOdd():
    try:
        num=int(input('수 입력 : '))
        if num%2 == 0:
            return 'even'

    except ValueError:
        print('수를 입력하세요!!!')
    except:
        print('에러 발생~!')

    finally:
        print('[무조건 출력] 함수 끝') 

    print('odd')    # return 없을 때 실행

# Main
n=EvenOdd()
print(n)    # even/odd 출력

# quiz 1 ) 나이입력!
# 쌤 코드! : 전체 코드 작성 후 예외처리만 밑에서 해주기~
while True:
    try:
       age = int(input('나이 입력 : '))
       st = str(age)
       if age >= 900101 or len(st) != 6:
           print('가입 불가')
       elif age <= 891231:
           print('가입 가능')
           break
    except:
        print('잘못 입력')

# quiz 2 ) 인증프로그램
# way 1
while True:
    print('---인증 프로그램---')
    try:
        id=input('주민번호 앞 자리 입력(예 900402)(종료 0) : ')
        if id == '0':
            break
        elif not id.isdigit():
            raise ValueError
        elif len(id) != 6:
            raise Exception

    except ValueError:
        print('잘못입력 숫자입력')
    except Exception:
        print('잘못입력 6자리 입력')
        
    else:
        if int(id[0:2]) >= 90:
            print(id, ': 가입불가')
        else:
            print(id, ': 가입가능')

# way 2
while True:
    print('---인증 프로그램---')
    try:
        id=input('주민번호 앞 자리 입력(예 900402)(종료 0) : ')
        if id == '0':
            break
        elif not id.isdigit():
            raise Exception('숫자입력')
        elif len(id) != 6:
            raise Exception('6자리 입력')

    except Exception as e:
        print('잘못입력 ',e)
        
    else:
        if int(id[0:2]) >= 90:
            print(id, ': 가입불가')
        else:
            print(id, ': 가입가능')

# 쌤 코드
try:
    min=input("주민번호 앞 자리 입력(예 900402) : ")
    if len(min) != 6:
        raise Exception("잘못 입력")
    if not min.isdigit():   #숫자로 구성되어 있냐
        raise Exception("잘못 입력 숫자 입력하세요")
    elif min[0] > '8':
        raise Exception(min)
except Exception as e:
    print(e,"가입불가")
else:
    print(min,":가입가능")
finally:
    print("프로그램 종료 합니다")
















