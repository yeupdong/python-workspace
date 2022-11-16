'''
지역변수(local variable)
- 특정 지역에서만 사용가능
전역변수(global variable)
- 코드 전체에서 사용가능
'''

# def function01():
#     global a
#     a = 100
#     print('function01 :',a)

# def function02():
#     #a = 200
#     print('function02 :',a)
    
# a = 1234
# function01()
# function02()

#변수의 이름만 같을 뿐 값은 다르다.
#전역 변수는 바깥라인에서 만드는 함수. 페이지 어디에서든 활용 가능.
#지역 변수와 전역 변수가 같은 변수이름을 사용하고 있을 때, 지역변수가 우선시 된다. 
#전역 변수 명시 = global a

# def func2(a,b):
#     a += 5; b *= 10;
#     print('func2 : a={}, b = {}'.format(a,b))

# def func1():
#     a = 5; b = 10
#     func2(a,b)
#     print('func1 : a={}, b={}'.format(a,b))
# func1()


# def display():
#     num = 10
#     print('10까지의 합 : ', sumFunc(num))

# def sumFunc(num):
#     sum_= 0
#     for i in range(num+1):
#         sum_ += i
#     return sum_
# display()

# def display():
#     sumFunc()
#     print('10까지의 합 : ', sum_)

# def sumFunc(num):
#     global sum_
#     for i in range(num+1):
#         sum_ += i
# num = 10; sum_ = 0;
# display()