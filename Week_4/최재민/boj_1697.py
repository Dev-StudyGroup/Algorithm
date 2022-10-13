from collections import deque

def bfs():
    q=deque()
    q.append(N)

    while q:
        a=q.popleft()
        if a == K:
            return visited[a]

        for j in (a-1,a+1,a*2):
            if(0 <= j < 100001) and visited[j] == 0:
                visited[j]=visited[a]+1
                q.append(j)

N,K = map(int,input().split())
visited=[0]*100001
print(bfs())




