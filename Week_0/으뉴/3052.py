import sys

input = sys.stdin.readline
left = set()
for i in range(10):
    left.add(int(input()) % 42)
    
print(len(left))
