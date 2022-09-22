import sys
input = sys.stdin.readline
a, b = input().split()
a=int(str(a)[::-1])
b=int(str(b)[::-1])
print(max(a,b))
