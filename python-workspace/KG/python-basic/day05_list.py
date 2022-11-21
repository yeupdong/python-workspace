'''
list
여거래의 값을 저장할 경우 사용
순서를 가지고 있다.
index는 0부터 시작한다. 
index를 변수로 이용 가능, 변수에 index를 활용 할 수도 있다.
[](대괄호)로 표현한다.
'''
# ls = [500,200,300,400]
# print (ls)
# print( ls[0], ls[3])

# ls = [0,0,0,0]
# ls[0] = int(input('0. 수 입력 : '))
# ls[1] = int(input('1. 수 입력 : '))
# ls[2] = int(input('2. 수 입력 : '))
# ls[3] = int(input('3. 수 입력 : '))
# sum_ = ls[0]+ls[1]+ls[2]+ls[3]
# print('합 :',sum_)

# ls = [0,0,0,0]
# sum_ = ls[0]+ls[1]+ls[2]+ls[3]
# for i in range(0,4):
#     ls[i] = int(input(f'{i}. 수 입력 : '))
#     sum_ += ls[i]
#     #print(str(i)+'수 입력 : ')
#     #print(f'{i}. 수 입력 : ')
# print('합 :',sum_)

# ls = [0,0,0,0]
# print('len :', len(ls))
#len() : 리스트의 길이를 측정해준다.
#for문을 이용할 때, range를 len()으로 해주면 좋다.

# for i in range(len(ls)):
#     print(f'ls[{i}] : {ls[i]}')

# for i in "abcd":
#     print(i)

# for i in ls:
#     print(i)

# ls = [10,20,30,40,50]
# print(ls)
# print('-'*10)
# print(ls[0:3])
# print(ls[2:])
# print(ls[:2])

ls = [[1,2,3],10,20,30,40]
#arr = ls #얕은 복사(전체를 공유)
#arr = ls[:] #깊은복사(데이터만 공유)
# arr = ls.copy()
# import copy
# arr = copy.deepcopy(ls)
# arr[0].append(4)
# print(ls, ' : ', id (ls))
# print(arr, ' : ', id(arr))



# #ls값을 저장하고 arr에 저장을 하였다.
# #대입을 시켰으니 두 값은 동일 하다.
# #id(정보)도 똑같이 나온다. 
# #ls전체 값이 저장이 되었고, id는 고유저장번호라고 보면 된다.
# #하나의 공간에 고유저장번호가 있고, 그 공간을 ls 와 arr 이 공유한다.

# #리스트 연산 (문자열 연산과 같다.)
# print('='*10)
# ls = [10,20,30]
# arr = [40,50,60]
# print(ls)
# print(arr)

# arr02 = ls + arr
# print(arr02)

# arr03 = ls * 3
# print(arr03)

# str = [0,0,0]
# string = [0,0,0]
# for i in range(len(ls)):
#     str[i] = ls[i] + arr[i]
# for i in range(len(ls)):
#     string[i] = ls[i] * 3
# print(str)
# print(string)

ls = [10,5,20,7,9,31,12,11,19,32]
evensum = [10,20,9,12,19]
oddsum = [5,7,31,11,32]
result = [0,0,0,0,0]
# for i in range(len(result)):
#     result[i]= evensum[i] - oddsum[i]
# print(result)
# print('='*20)
# for j in range(len(oddsum)):
#     #print(f'{oddsum[0]+oddsum[1]+oddsum[2]+oddsum[3]+oddsum[4]}')
#     oddsum_ = f'{oddsum[0]+oddsum[1]+oddsum[2]+oddsum[3]+oddsum[4]}'
# print(oddsum_)

# for k in range(len(evensum)):
#     evensum_ = f'{evensum[0]+evensum[1]+evensum[2]+evensum[3]+evensum[4]}'
# print(evensum_)
# print(int(oddsum_)+int(evensum_))
# print(int(oddsum_)-int(evensum_))
# print('='*20)

# ls = [10,5,20,7,9,31,12,11,19,32]
# evensum = [10,20,9,12,19]
# oddsum = [5,7,31,11,32]
# result = [0,0,0,0,0]
# index = 0
# esum = 0
# osum = 0

# for i in range(len(ls)):
#     if i % 2 == 0:
#         evensum[index] = ls[i]
#     else:
#         oddsum[index] = ls[i]
#         index += 1
# print(evensum)
# print(oddsum)

# for i in range(len(evensum)):
#     result[i] = evensum[i] - oddsum[i]
# print(result)

# for i in range(len(evensum)):
#     esum += evensum[i]
#     osum += oddsum[i]
# print(f'{esum}-{osum}={esum-osum}')

# j = len(ls)
# invertLs = [0,0,0,0,0,0,0,0,0,0]
# for i in ls:
#     j-=1
#     invertLs[j] = i
# print(invertLs)

# ls = [82, 85, 76, 79, 96]
# rank = [1, 1, 1, 1 ,1]
# index = 0

# for i in range(len(ls)):
#     for k in range(len(rank)):
#         if ls[i] < ls[k]:
#             rank[i] += 1

# print(rank)
