import sys
sys.setrecursionlimit(10**6)

#입력
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    arr=[[0]*m for i in range(n)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        arr[y][x]=1
    
    #배추흰지렁이 마리수 카운트
    count=0
    
    #상하좌우
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    
    #dfs정의
    def dfs(y,x):
        #x와 y의 범위가 땅의 크기를 벗어나는 경우,
        if y<0 or x<0 or y>=n or x>=m:
            return
        elif arr[y][x]==1:
            arr[y][x]=0
            for i in range(4):
                m_x = x+dx[i]
                m_y = y+dy[i]
                dfs(m_y,m_x)
    #dfs실행
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                count+=1
                dfs(i,j)
    
    #출력
    print(count)
    
