# def big(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# result = big(10,20)
# print(result)

# print('='*20)

# bi = lambda a,b: a if(a>b) else b
# result = bi(200,1000)
# print(result)

# print('='*20)

# bi = lambda a : a+1000
# print(bi(100))

# li = ['100','200','300']
# for i in li:
#     li[i] = str(int( li[i]+10 ))

# li = ['100','200','300']
# li = list(map(int,li))
# for i in li:
#     li[i] = str(li[i]+10)


# li = ['100','200','300']
# def test1(a):
#     return str( int(a)+10)

# li = list(map(test1, li))
# print('함수 : ', li)

# print('='*20)

# li = ['100','200','300']
# lb = lambda x : str( int(x)+1000)

# li = list ( map(lambda x : str( int(x)+1000),li))
# print("lambda :", li)

day = {'날짜':['2018.01.01','2019.02.02','2020.03.03']}

for key,values in day.items():
    for i in values:
        #print(i)
        v = i.split(".")
        #print(v)
        print(f'{v[0]}년 {v[1]}월 {v[2]}일')

ls = list(map(lambda x : x.split("."), day['날짜']))
for i in ls:
    print(f'{i[0]}년 {i[1]}월 {i[2]}일')