'''
#append
ls = list()
for i in range(3):
    value = input(f'{i}.번째 입력 : ')
    ls.append(value)
print('총 개수 : ', len(ls))
print('type :', type(ls))
print('ls : ', ls)

ls = []
print('초기화 후 ls : ',ls)

ls = [30,10,20,40]
print('ls : ', ls)
ls.pop()
print('pop : ', ls) #[30,10,20] 제일 마지막에 있는 값을 뺌.
ls.reverse()
print('reverse : ',ls) #[20,10,30] 역순으로 재배치
ls.sort()
print('sort : ', ls) #[10,20,30] 오름차순 정렬

ls = [10,20,30]
print('ls : ', ls)
del( ls[1] ) 
print('del(ls.1) :', ls) #해당 인덱스 값을 삭제
ls.remove( 30 )
print( 'remove(30) :', ls)

ls = [30,20,10]
print(ls)
i = ls.index(20)
print('index(20) :', i) #있는 값에 한해서 인덱스 값을 보여줌.

ls.append(100)
print('append(100) :', ls) #append는 무조건 제일 마지막에 추가된다.

ls.insert(2,500)
print('insert(index,value)', ls) #지정된 인덱스 위치에 새로운 값을 더해줌.

arr = [1,2,3,1]
#ls = ls + arr
ls.extend(arr)
print('ls.extend', ls) #리스트 뒤에 값을 더해줌

cnt = ls.count(1)
print('count(value) : ', cnt) #같은 값의 갯수를 찾아줌.
'''

ls = [10,50,70,30,20]
#arr : ls가 가지고 있는 값을 역으로 저장
#sort_arr : 오름차순으로 저장
#rever_arr : 내림차순으로 저장
# arr = ls.reverse()
# print(ls)
# sort_arr = ls.sort()
# print(ls)
# rever_arr = ls.reverse()
# print(ls)

# arr = ls.copy()
# print('ls : ', ls)
# arr.reverse()
# print('arr : ', arr)
# sort_arr = ls.copy()
# sort_arr.sort()
# print('sort_arr : ', sort_arr)
# reverse_arr = ls.copy()
# reverse_arr.sort()
# print('sort :', reverse_arr)
# reverse_arr.reverse()
# print('reverse :', reverse_arr)




ls = [10,20,30]
s = ls[0] * 100
print(s)

ls = ['10','20','30']
s = int(ls[0]) + 100 #인덱스의 값이 문자열일때, 정수형태로 바꿔줘야한다.
print(s)

'''
ls = ['10','20','30']
print('변환전 :', ls)
s = list(map(int, ls))
print('변환 후 :', s)

or

ls = ['10','20','30']
s = []
for i in ls:
    s.append( int(i))
print(ls)
print(s)
'''