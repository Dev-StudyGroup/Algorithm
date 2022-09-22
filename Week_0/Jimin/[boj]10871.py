'''
'X보다 작은 수'
'''
N, X = map(int, input().split())
answer_list = []
A = list(map(int, input().split()))

for i in A:
    if i < X:
        answer_list.append(i)

print(*answer_list)