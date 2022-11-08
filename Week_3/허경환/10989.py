import sys
#입력
n = int(input())
count=[0]*10001
for i in range(n):
    count[int(sys.stdin.readline().strip())]+=1

#출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i)
