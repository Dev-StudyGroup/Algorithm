import sys

#입력
t = int(input())
for _ in range(t):
    n = int(input())
    ls=[(1,0), (0,1)]
    for i in range(2, n+1):
        ls.append((ls[-1][0]+ls[-2][0], ls[-1][1]+ls[-2][1]))
    if n==0:
        print(1,0)
    else:
        print(ls[-1][0], ls[-1][1])
