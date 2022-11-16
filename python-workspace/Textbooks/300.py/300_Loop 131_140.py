#131
print('{:=^30}'.format('#131'))
#for문의 실행결과를 예측하라.
fruit = ["apple", 'mandarin', 'watermelon']
for variables in fruit:
    print(variables)

#132
print('{:=^30}'.format('#132'))
#for문의 실행결과를 예측하라.
fruit = ["apple", 'mandarin', 'watermelon']
for variables in fruit:
    print("#####")

#133
print('{:=^30}'.format('#133'))
#다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
for variables in ["A","B","C"]:
    print(variables)
'''
variables = "A"
print(variables)
variables = "B"
print(variables)
variables = "C"
print(variables)

or

print("A")
print("B")
print("C")
'''

#134
print('{:=^30}'.format('#134'))
#for문을 풀어서 동일한 동작을하는 코드를 작성하라.
for variables in ["A","B","C"]:
    print("print:", variables)

'''
print("print:", "A")
print("print:", "B")
print("print:", "C")
'''

#135
print('{:=^30}'.format('#135'))
#for문을 풀어서 동일한 동작을 하는 코드를 작성하라.

for variables in ["A","B","C"]:
    b = variables.lower()
    print("transform :", b)

'''
variables = "A"
b = variables.lower()
print("transform :", b)
variables = "B"
b = variables.lower()
print("transform :", b)
variables = "C"
b = variables.lower()
print("transform :", b)
'''

#136
print('{:=^30}'.format('#136'))
#다음 코드를 for문으로 작성하라.
'''
variables = 10
print(variables)
variables = 20
print(variables)
variables = 30
print(variables)
'''
for variables in [10,20,30]:
    print(variables)

#137
print('{:=^30}'.format('#137'))
#다음 코드를 for문으로 작성하라.
'''
print(10)
print(20)
print(30)
'''
for variables in [10,20,30]:
    print(variables)

#138
print('{:=^30}'.format('#138'))
#다음 코드를 for문으로 작성하라.

'''
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")
'''

for variables in [10,20,30]:
    print(variables)
    print("-------")

#139
print('{:=^30}'.format('#139'))
#다음 코드를 for문으로 작성하라.

'''
print("++++")
print(10)
print(20)
print(30)
'''

for variables in ["\"++++\"",10,20,30]:
    print(variables)

print("++++")
for variables in [10,20,30]:
    print(variables)

#140
print('{:=^30}'.format('#140'))
#다음 코드를 for문으로 작성하라.
#**파이썬 for문은 들여쓰기된 코드가 자료구조의 데이터 개수만큼 반복된다는 사실이 중요합니다.** 

'''
print("-------")
print("-------")
print("-------")
print("-------")
'''

for i in [1,2,3,4]:
    print("-------")