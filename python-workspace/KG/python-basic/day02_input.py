#형변환
num1 = input('수 입력 :')
print('입력 값 :', num1)
print('\t')
print('\t')
#Question
name = input('이름을 입력하세요 :')
age = input('나이를 입력하세요 :')
print(f'{name}님은 {age}세 입니다.')
print('{}님은 {}세 입니다.'.format(name,age))
print('\t')
print('\t')
print('두 수의 합을 구해줍니다.')
n1 = int(input('첫번째 수 입력 :'))
n2 = int(input('두번째 수 입력:'))
s = n1 + n2
print(f'두 수의 합: {n1} + {n2} = {s}')
print('\t')
print('\t')
#Question
thisyear = int(input('올해의 년도를 입력하세요 :'))
yob = int(input('당신이 태어난 년도를 입력하세요 :'))
age = thisyear - yob
print(f'당신의 나이는 {age}살 입니다.')
print('\t')
print('\t')
lift = 600
fstcar = float(input('첫번째 물건의 무게를 입력하세요. :'))
sndcar = float(input('두번째 물건의 무게를 입력하세요. :'))
weight = lift - fstcar - sndcar
print(f'현재 엘리베이터 허용 무게는 {weight}kg입니다.')
print('\t')
print('\t')
height = int(input('현재 키를 입력하세요. :'))
avgweight = (height - 100)*0.9
print(f'표준 체중은 {round(avgweight,2)}kg입니다.')
crtweight = int(input('현재 체중을 입력하세요. :'))
fatrate = (crtweight/avgweight)*100
print(f'표준체중은 {round(avgweight,2)}이고 비만도는 {round(fatrate,2)}%입니다.')
print('\t')
print('\t')
name = str(input('이름을 입력하세요. :'))
kor = int(input('국어점수를 입력하세요. :'))
eng = int(input('영어점수를 입력하세요. :'))
math = int(input('수학점수를 입력하세요. :'))
total = kor + eng + math
avg = round(total / 3,2)
print('<결과>')
print('학생 이름', name)
print('국어점수', kor)
print('영어점수', eng)
print('수학점수', math)
print(f'{"학생정보":=^47}')
print('이름\t국어\t영어\t수학\t합계\t평균')
print('='*50)
print(f'{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg}')
