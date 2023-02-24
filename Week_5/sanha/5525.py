N = int(input())
M = int(input())
S = input().rstrip()

ioi = 0
cnt = 0
cur = 1
while cur < M - 1:
    if S[cur - 1] == 'I' and S[cur] == 'O' and S[cur + 1] == 'I':
        ioi += 1
        if ioi == N:
            ioi -= 1
            cnt += 1
        cur += 1
    else:
        ioi = 0
    cur += 1

print(cnt)
