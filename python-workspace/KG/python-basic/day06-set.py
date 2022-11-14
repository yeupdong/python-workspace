'''
set - 하나의 자료형
- 중복된 데이터 허용하지 않음.
- 순서를 유지하지 않는다.
- 모양은 dictionary와 같지만, 사용방법은 다르다.

사용 방법
-set(데이터)
-{값,값,값...}
'''

s = {"안녕하세요"} 
print(s) #출력값에서는 왜 ' 로 나오는가? 
print(type(s))

s = set([1,1,1,2,3,4,4])
print(s) # {1, 2, 3, 4}
#print(s[0]) #인덱스로 접근이 불가능하다. 형변환을 해줘야 한다.

ls = list(s)
print(ls)
print(ls[0])

s = {1,2,3}
print('변경 전', s)
s.add(555)
print('변경 후', s)

s.update([4,5,6])
print(s)

s.remove(555)
print('remove(555) :', s)
print("issuperset :", s.issuperset({1,2}))