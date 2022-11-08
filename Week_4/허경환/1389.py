from collections import deque
#입력
n, m = map(int, input().split())
arr=[[0]*(n+1) for i in range(n+1)]
connect = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    if a not in connect[b]:
        connect[b].append(a)
    if b not in connect[a]:
        connect[a].append(b)

#각 사람을 기준으로 나머지 사람들과의 각각 거리의 합을 구하기
#최단거리
#가중치가 없는 그래프의 최단거리 -> bfs
def bfs(start):
    queue = deque([])
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i in connect[now]:
            if i==start:
                continue
            if arr[start][i]!=0:
                continue
            else:
                queue.append(i)
                arr[start][i]+=(arr[start][now]+1)

    
    

#각 유저를 시작점으로 실행
for i in range(1,n+1):
    bfs(i)
    
#케빈 베이컨의 수가 가장 작은 사람을 찾기
answer=[0]*(n+1)
for i in range(1,n+1):
    answer[i]=sum(arr[i])
answer=answer[1:]
print(answer.index(min(answer))+1)
