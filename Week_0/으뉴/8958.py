import sys

arr = []
n = int(input())
for i in range(n):
    arr.append(input())

for i in range(n):
    cnt, total = 0, 0
    for a in arr[i]:
        if a == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)
            
        
