'''
튜플
- 중복을 허용하지 않는다.
- 데이터의 변경이 불가능하다.
- index접근 가능하다.
- (소괄호)로 표현한다.
'''

tp = (10,20,30)
print(tp)
print(type(tp))
print(tp[0])
print(len(tp))
#tp[0] = 1234 #데이터 변경 불가능.
tp = (10) #튜플 전체의 데이터 변경은 가능.
print(tp,":", type(tp))

tp = (10,) #" , "를 기준으로 튜플로 표현을 할 것인지, 다른 표현을 할 것인지 결정.
print(tp,":", type(tp))

tp = 10, #" , "를 기준으로 튜플로 표현을 할 것인지, 다른 표현을 할 것인지 결정.
print(tp,":", type(tp))

'''
패킹: 압축(여러개의 값을 하나의 공간에 저장)
언패킹: 하나의 덩어리를 여러개의 공간에 저장 
'''
#패킹 예)
tp = 1,2,"패킹",3,4,5
print("패킹", tp)
#언패킹 예)
a,b,c,d,e,f = tp
print(a,b,c,d,e,f)

a,b,*c = tp #tp의 저장값이 하나씩 옮겨지고, c부터는 리스트로 한꺼번에 묶어준다. 1 2 ['패킹',3,4,5]
print(a,b,c)

tp = 100,200,300,100
print(tp.count(100)) #해당값의 갯수를 세어줌
print(tp.index(200)) #인덱스의 위치를 보여줌
