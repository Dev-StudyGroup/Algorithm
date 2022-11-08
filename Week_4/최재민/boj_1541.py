import sys

num = sys.stdin.readline().split('-')
minus = []

for i in num:
    cnt = 0
    num1 = i.split('+')
    for j in num1:
        cnt += int(j)
    minus.append(cnt)

answer = minus[0]

for i in range(1, len(num)):
    answer -= minus[i]

print(answer)
