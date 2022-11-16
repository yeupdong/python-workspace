#print
print('test python')
print(3+5)
print('안녕하세요')
#escape
print('안\n녕\n하\n세\n요')
print('1\t1234567\t12345678\t1')
print('\t')
print('\t')
print('이름\t나이\t주소')
print("a''''a")
print('a""""a')
print("안녕\"하세요")
print('\\')
print('\t')
print('\t')
#Question
print('\t\t####회비정보####')
print('='*50)
print('이름\t\t나이\t전화번호\t회비')
print('='*50)
print('홍길동\t\t"15"\t010-123-1234\t\\20,000')
print('임꺽정\t\t"20"\t010-234-2345\t\\30,000')
print('김말이\t\t"28"\t010-345-3456\t\\50,000')
print('-'*50)
print('총합계\t\t\t\t\t\\100,000')
print('='*50)
print('\t')
print('\t')
#string+integer?
print('안녕하세요'+'ㅁㅁㅁㅁ')
print(100+100)
print(10/2, '입니다', 10+10)
print('\t')
print('\t')
#comma 
print('12+54 =', 12+54, '입니다.')
print('268-42 =', 268-42, '입니다.')
print('2*23 =', 2*23, '입니다.')
print('120/3 =', 120/3, '입니다.')
print('\t')
print('\t')
#format
print(f'3+5={3+5} 입니다.')
print('3+5={} 입니다.'.format(3+5))
print('{} + {} = {}'.format(10,20,10+20))
print('{2} + {0} = {1}'.format(10,20,10+20))
print('{:,}'.format(1000000000)) #숫자에 , 넣기
print('{:>10},{:0<10}'.format('1번째','2번째')) #왼쪽 정렬
print('{:<10},{:8>10}'.format('1번째','2번째')) #오른쪽 정렬
print('{:^10},{:5^10}'.format('1번째','2번째')) #가운데 정렬
print('\t')
print('\t')