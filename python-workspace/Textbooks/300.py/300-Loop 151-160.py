#151
print('{:=^30}'.format('#151'))
#리스트에는 네 개의 정수가 저장돼 있다.
#ls = [3, -20, -3, 44]
#for문을 사용해서 리스트의 음수를 출력하라.

ls = [3, -20, -3, 44]
for i in range(len(ls)):
    if ls[i] < 0:
        print(ls[i])

#152
print('{:=^30}'.format('#152'))
#for문을 사용해서 3의 배수만을 출력하라.
#ls = [3, 100, 23, 44]

ls = [3, 100, 23, 44]
for i in ls:
    if i % 3 == 0:
        print(i)

#153
print('{:=^30}'.format('#153'))
#리스트에서 20 보다 작은 3의 배수를 출력하라
#ls = [13, 21, 12, 14, 30, 18]

ls = [13, 21, 12, 14, 30, 18]
for i in ls:
    if i < 20 and i % 3 == 0:
        print(i)

#154
print('{:=^30}'.format('#154'))
#리스트에서 세 글자 이상의 문자를 화면에 출력하라
#ls = ["I", "study", "python", "language", "!"]

ls = ["I", "study", "python", "language", "!"]
for i in ls:
    if len(i) > 3:
        print(i)

#155
print('{:=^30}'.format('#155'))
#리스트에서 대문자만 화면에 출력하라.
#ls = ["A", "b", "c", "D"]
#(참고) isupper() 메서드는 대문자 여부를 판별합니다.

ls = ["A", "b", "c", "D"]
for i in ls:
    if i.isupper():
        print(i)

#156
print('{:=^30}'.format('#156'))
#리스트에서 소문자만 화면에 출력하라.
#ls = ["A", "b", "c", "D"]

ls = ["A", "b", "c", "D"]

for i in ls:
    if i.isupper() == False:
        print(i)

for i in ls:
    if i.isupper() != True:
        print(i)

for i in ls:
    if not i.isupper():
        print(i)

#157
print('{:=^30}'.format('#157'))
#이름의 첫 글자를 대문자로 변경해서 출력하라.
#ls = ['dog', 'cat', 'parrot']

ls = ['dog', 'cat', 'parrot']

