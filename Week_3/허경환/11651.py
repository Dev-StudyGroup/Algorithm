import sys
#입력
n = int(input())
point=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

#정렬
point.sort(key=lambda x : (x[1],x[0]))

#출력
for i in point:
    print(i[0], i[1])
