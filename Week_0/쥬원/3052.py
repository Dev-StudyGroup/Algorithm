import sys
input = sys.stdin.readline
t = set()
for _ in range(10):
    t.add(int(input())%42)
print(len(t))
