'''
f5: debugging
f9: break point
f11: one line
f10: one line
shift+f5: end debugging'''

sum_ = 0
for i in range(100000):
    sum_ += i
print(sum_)
print(sum_)
print(sum_)
print(sum_)

for i in range(5):
    print('실행')
    for k in range(3):
        print('종속')
    print('끝')

