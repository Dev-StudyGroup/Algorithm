N = int(input())

space = 1
cnt = 1
while N>space:
    space += 6 * cnt
    cnt += 1

print(cnt)