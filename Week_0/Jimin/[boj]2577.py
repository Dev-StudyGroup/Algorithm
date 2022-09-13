'''
'숫자의 개수'
'''
A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result = str(result)

cnt_list = [0] * 10
for i in result:
    cnt_list[int(i)] += 1

for i in cnt_list:
    print(i)