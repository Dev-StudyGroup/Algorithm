'''
'덩치'
'''
N = int(input())
body = []
for i in range(N):
    body.append(list(map(int, input().split())))

answer = []
for i in range(N):
    rank = 1
    w1, h1 = body[i]
    for j in range(N):
        if i == j:
            continue
        else:
            w2, h2 = body[j]
            if w1 < w2 and h1 < h2:
                rank += 1
    answer.append(rank)

print(*answer)
