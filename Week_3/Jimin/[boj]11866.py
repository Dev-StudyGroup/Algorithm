'''
'요세푸스 문제 0'
'''
N, K = map(int, input().split())

array = [i for i in range(1, N+1)]
answer = []

present = K - 1
while True:
    answer.append(array[present])
    array = array[:present]+array[present+1:]

    if len(array) == 0:
        break

    present = (present + K-1) % len(array)

print('<', end = '')
for i in range(N):
    if i == N-1:
        print(str(answer[i])+'>', end = '')
    else:
        print(str(answer[i])+', ', end = '')
