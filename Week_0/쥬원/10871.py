import sys
input = sys.stdin.readline
_, x = map(int, input().split())
t=list(map(int,input().split()))
for i in t:
    if i < x:
        print(i, end=" ")
