import sys
N = int(input())

meet = []

for _ in range(N):
    meet.append(list(map(int,sys.stdin.readline().split())))

meet = sorted(meet, key=lambda a: a[0])
meet = sorted(meet, key=lambda a: a[1])

last = 0
cnt = 0

for i, j in meet:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
