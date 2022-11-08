import sys
import heapq
#입력
n = int(sys.stdin.readline().rstrip())
ls=[]
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x!=0:
        heapq.heappush(ls, x)
    else:
        if ls==[]:
            print(0)
        else:
            num=heapq.heappop(ls)
            print(num)

