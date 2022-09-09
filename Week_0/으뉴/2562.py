import sys

arr = []
for _ in range(9):
    arr.append(sys.stdin.readline())
    
print(max(arr))
print(arr.index(max(arr))+1)
