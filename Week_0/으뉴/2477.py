import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
res = str(a*b*c)

for i in range(10):
    print(res.count(str(i))) # res 문자열 내 i 개수
