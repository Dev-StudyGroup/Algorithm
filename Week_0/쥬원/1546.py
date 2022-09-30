import sys
input = sys.stdin.readline
n = int(input())
t = list(map(int, input().split()))
m = max(t)
a = 0
for i in t:
    a += i/m*100
print(a/n)
