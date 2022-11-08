import sys

#입력
k = int(input())
ls=[0]
for _ in range(k):
    n = int(sys.stdin.readline().rstrip())
    if n==0:
        ls.pop()
    else:
        ls.append(n)

#출력
print(sum(ls))
