import sys
input = sys.stdin.readline
t = []
for i in range(9):
    t.append(int(input()))
print(max(t))
print(t.index(max(t))+1)
