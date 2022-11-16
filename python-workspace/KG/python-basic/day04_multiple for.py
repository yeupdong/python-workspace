# for i in range(0,3,1):
#     print('상위 for문 실행')
#     for k in range(0,5,1):
#         print(f'이중 for 문 (i:{i}, k:{k})')
#     print('종료 상위 for문')

#구구단 만들기

# for i in range(2,10,1):
#     for k in range(1,10,1):
#         print(f'{i}*{k}={i*k}',end='\t')


# 상위 포문 0 일때 하위 포문 : 0 0 0 0 0 
# 상위 포문 1 일때 하위 포문 : 0 1 2 3 4
# 상위 포문 2 일때 하위 포문 : 0 2 4 6 8
# 상위 포문 3 일때 하위 포문 : 0 3 6 9 12
# 상위 포문 4 일때 하위 포문 : 0 4 8 12 16

# for i in range(0,5):
#     print(f'상위 포문 {i} 일때 하위 포문 :', end=' ')
#     for k in range(0,5):
#         print(f'{i*k}', end=' ')
#     print()

# 1       2       3       4       5
# 6       7       8       9       10
# 11      12      13      14      15
# 16      17      18      19      20
# 21      22      23      24      25
# for i in range(1,26,5):
#     print(i,end='\t')
#     for k in range(1,5):
#         print(i+k, end='\t')
#     print()