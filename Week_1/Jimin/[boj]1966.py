'''
'프린터 큐'
'''
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    answer = 1
    idx = M

    while True:
        j = p[0]
        if j < max(p):
            if idx == 0:
                idx = len(p)-1
            else:
                idx -= 1
            p = p[1:]
            p.append(j)
        else:
            if idx == 0:
                break
            p = p[1:]
            answer += 1
            idx -= 1

    print(answer)
