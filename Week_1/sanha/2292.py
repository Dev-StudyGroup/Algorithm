N = int(input())
cnt = 1
blocks = 1
while N > blocks:
    blocks += cnt * 6
    cnt += 1
print(cnt)
