'''
반복문
어 떤 내용을 반복하고자 하는 경우
규칙적으로 값이 변경 된다면
for 변수 in range(초기값, 비교값, 증감값)
    종속문장
'''

# num = 0
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)
# num += 1; print(num)

# for i in range(0,11,1): #(i=0, i<11, i=i+1)
#     print(i)
# print('proceed to next')

#짝수값 출력
# for i in range(1,11,1): #(i=1, i<11, i=i+1)
#     if i % 2 == 0:
#         print('i =',i)
# print('다음문장실행')

# end 활용법
# print('안녕', end='(변경값)')
# print('하세')
# print('요')

# total = 0
# for num in range(1,11,1):
#     total = total + num
# print(total)

# for i in range(1,31,1):
#     print(i, end='\t')
#     if i % 5 == 0:
#         print()

# num = int(input('input any number :'))
# even = 0
# odd = 0
# for i in range(1,num+1,1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(even)
# print(odd)

# for i in range(10):
#     print(i,end=', ')
# print()

# num1 = int(input('enter 1st number :'))
# num2 = int(input('enter 2nd number :'))
# sum_ = 0

# for i in range(num1,num2+1):
#         sum_ += i;
# for i in range(num2,num1+1):
#         sum_ += i;
# print(sum_)

# if num1 > num2:
#     max_, min = num1, num2
# else:
#     max_, min = num2, num1
# sum_ = 0
# for i in range(min ,max_+1):
#     sum_ += i
# print('total',sum_)

# st = 'hello python'
# for i in st:
#     print(i)

# st = 'It is a fun Python class'
# cnt_a = 0
# cnt_s = 0
# cnt = 0
# for i in st:
#     if i == 'a':
#         cnt_a += 1
#     elif i == 's':
#         cnt_s += 1

# print(f'총 개수: {len(st)}')
# print(f'a 개수: {cnt_a}')
# print(f's 개수: {cnt_s}')