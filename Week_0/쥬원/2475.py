import sys
input=sys.stdin.readline
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i**2
print(s%10)
