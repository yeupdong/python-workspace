# 1차원 리스트 : ls = [value, value, value] 
# 다차원 리스트 : ls = [[value], [value], [value]]

# ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# print( ls[0] ) # [1,2,3,4] 콤마를 기준으로 값을 판단해야 한다.
# print( ls[0][1] ) # 2, 0번째 인덱스(첫번째 리스트) 안에 있는 1번째 인덱스

# ls = [[1,[2,100,200],3,4], [5,6,7,8], [9,10,11,12]]
# print( ls[0][1][2]) # 200


# ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# print( ls[0][0] ) #1
# print( ls[0][1] ) #2
# print( ls[0][2] ) #3
# print( ls[0][3] ) #4
# print( ls[1][0] ) #5
# print( ls[1][1] ) #6
# print( ls[1][2] ) #7
# print( ls[1][3] ) #8


# ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# for i in range(3): #or for i in range(len(ls))
#     for k in range(4): #or for k in range(len(ls[i]))
#         print(ls[i][k], end=' ')
#     print()

# ls = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# for i in ls:
#     for k in i:
#         print(k, end=" ")
#     print()

#ls = [[1,2,3,4],[5,6,7,8]]
#arr = ls[0] #얕은복사(1)
#arr = ls[0][:] #얕은복사(2)
#arr = ls[0].copy() #얕은복사(3)
#arr[1] = 1000
#print(ls)
#print(arr)

# ls_1 = []
# ls_2 = []
# value = 1

# for k in range(3):
#     ls_1=[]
#     for i in range(4):
#         ls_1.append(value)
#         value+=1
#     ls_2.append(ls_1)

# #print(ls_1)
# #print('ls_2 :', ls_2)

# for i in range(3):
#     for k in range(4):
#         print(ls_2[i][k], end=' ')
#     print()
# print('ls_2 :', ls_2)

# while value < 13:
#     ls_1.append( value )

#     if value%4 == 0:
#         ls_2.append( ls_1 )
#         ls_1 = []
#     value += 1
# print( ls_2 )

print('{:=^40}'.format('이름 프로그램'))
