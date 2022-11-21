'''
dict
- key/value 쌍
- {} 중괄호
- 탐색 속도 빠름
- 사용하기 편리하다
methods
https://www.w3schools.com/python/python_dictionaries_methods.asp
'''

dic={'num':'eng', 1:'one', 2:'two', 3:'three'}
print(dic)

print(dic['num'])   # eng
print(dic[1])       # one

'''
dict 추가
- dict[key] = value                 # 무조건 추가
- dict.setdefault( key, value )     # 해당키가 없으면 추가, 있으면 추가 X
'''

dic[4] = 'four'
dic.setdefault(5, 'five')

# 각각 type : dict_keys , dict_values , dict_items
dic.keys()      # [ key1, key2, ... ]
                # dict_keys(['num', 1, 2, 3, 4, 'end'])
dic.values()    # [ value1, value2, ... ]
                # dict_values(['eng', 'one', 'two', 'three', 'four', 'final'])
dic.items()     # [ (key1, value1), (key2, value2), ... ]
                # dict_items([('num', 'eng'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), ('end', 'final')])

for i in dic.keys():    # dic의 key들
    print(i, ':', dic[i])   # i: keys(), dic[i]: values()

for k, v in dic.items():
    print(f'{k} : {v}')     # 예쁘게 출력됨. key1 : value1
                            #               key2 : value2  ...

'''
dict 출력하기
- dict[key]          : 없으면 error
- dict.get(key)      : 없으면 None
'''
#print(dic[8])   # error
dic.get(8)      # None

index=int(input('key 입력 : '))
result = dic.get(index)     # 있으면 value값, 없으면 None
if result == None:
    print('없습니다.')
else:
    print(result)

'''
list와 dict
'''
# dict 안에 list
school = {'id':[1, 2, 3] , 'class':'A'}
print(school['class'])     # A
print(school['id'])        # [1,2,3]

# lsit 안에 dict
QandA = [1, {'math':'30번'}, 3]
QandA[1]            # {'math':'30번'}
QandA[1]['math']    # 30번

# dict 안에 dict
pop={}
kpop={}

kpop['singer']='bb'
kpop['rank']=4
kpop['album']='hi'

pop[kpop['singer']] = kpop    # 얕은 복사 : kpop 바꾸면 pop도 같이 바뀜

kpop    # {'singer': 'bb', 'rank': 4, 'album': 'hi'}
pop     # {'bb': {'singer': 'bb', 'rank': 4, 'album': 'hi'}}

for k, v in kpop.items():   # pop에서 'bb'와 {'singer':'bb', ...}
    for kk, vv in v.items():    # {'singer':'bb', ...}에서 singer와 bb ...
        print(kk, ':', vv)

pop[kpop['singer']] = kpop.copy()   # 깊은 복사 : kpop만 수정되고 pop은 그대로

'''
dict 초기화
dict={}
dict.clear()
'''

