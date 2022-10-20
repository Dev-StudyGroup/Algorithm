N = int(input())
cnt = 0
flag = False

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        flag = True
        break
    N -= 3
    cnt += 1

if flag:
    print(cnt)
else:
    print(-1)
