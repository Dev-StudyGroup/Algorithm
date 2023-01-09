from collections import deque
from collections import defaultdict

N, M = map(int, input().split())

ladders = defaultdict()
snakes = defaultdict()
G = [0] * 101
visited = [False] * 101

for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

q = deque([1])
visited[1] = True

while q:
    x = q.popleft()
    if x == 100:
        print(G[x])
        break

    for dice in range(1, 7):
        nx = x + dice
        if nx in ladders.keys():
            nx = ladders[nx]
        if nx in snakes.keys():
            nx = snakes[nx]

        if nx <= 100 and not visited[nx]:
            G[nx] = G[x] + 1
            q.append(nx)
            visited[nx] = True
