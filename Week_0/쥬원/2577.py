import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
t = str(a*b*c)
for i in range(10):
    print(t.count(str(i)))
