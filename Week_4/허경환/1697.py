from collections import deque

#입력
n, k = map(int, input().split())

#문제유형파악 -> 최단거리 BFS

#방문체크
visited=[False]*100001

ans=0

#bfs정의
def bfs(n, k, visited):
    global ans
    
    #큐 생성
    queue = deque([])
    queue.append((n,0))
    
    while queue:
        now, count = queue.popleft()
        #방문체크하기
        visited[now]=True
        
        #현재노드가 k라면
        if now==k:
            ans=count
            return 
    
    
        if 0<=now-1<=100000 and visited[now-1]==False :
            queue.append((now-1, count+1))
        if 0<=now+1<=100000 and visited[now+1]==False:
            queue.append((now+1, count+1))
        if 0<=now*2<=100000 and visited[now*2]==False:
            queue.append((now*2, count+1))
    
    
#bfs실행
bfs(n, k, visited)


#출력
print(ans)
