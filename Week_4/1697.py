"""
1697: 숨바꼭질
"""
from collections import deque

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break 
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 10 ** 5 and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
        
# n: 수빈이의 위치(<= 100,000), k: 동생의 위치(<= 100,000)
n, k = map(int, input().split())
dist = [0] * (10 ** 5 +1)

bfs()
