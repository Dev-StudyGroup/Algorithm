# 문제
# 마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전할 수 있다. 오늘은 파이어스톰을 크기가 2N × 2N인 격자로 나누어진 얼음판에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다. A[r][c]가 0인 경우 얼음이 없는 것이다.
#
# 파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다. 파이어스톰은 먼저 격자를 2L × 2L 크기의 부분 격자로 나눈다. 그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다. 아래 그림의 칸에 적힌 정수는 칸을 구분하기 위해 적은 정수이다.
#
# 마법을 시전하기 전	L = 1	L = 2
#
# 마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다. 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.
#
# 남아있는 얼음 A[r][c]의 합
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.
#
# 입력
# 첫째 줄에 N과 Q가 주어진다. 둘째 줄부터 2N개의 줄에는 격자의 각 칸에 있는 얼음의 양이 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
#
# 마지막 줄에는 마법사 상어가 시전한 단계 L1, L2, ..., LQ가 순서대로 주어진다.
#
# 출력
# 첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다. 단, 덩어리가 없으면 0을 출력한다.
#
# 제한
# 2 ≤ N ≤ 6
# 1 ≤ Q ≤ 1,000
# 0 ≤ A[r][c] ≤ 100
# 0 ≤ Li ≤ N
import copy
from collections import deque
n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
ls = list(map(int, input().split()))
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[False for _ in range(2**n)] for _ in range(2**n)]
def tornado(l):
    global grid
    result = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for i in range(0, 2**n, 2**l):
        for j in range(0, 2**n, 2**l):
            tmp = []
            for k in range(i, i+2**l):
                tmp.append(grid[k][j:j+2**l])
            new_tmp = list(zip(*tmp[::-1]))
            for k in range(i, i+2**l):
                for m in range(j, j+2**l):
                    result[k][m] = new_tmp[k-i][m-j]
    grid = copy.deepcopy(result)
def melt_ice():
    global grid
    result = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            if grid[i][j]:
                cnt = 0
                for d in range(4):
                    ni, nj = i+dy[d], j+dx[d]
                    if 0 <= ni < 2**n and 0 <= nj < 2**n:
                        if grid[ni][nj]:
                            cnt += 1
                if cnt < 3:
                    result[i][j] = grid[i][j]-1
                else:
                    result[i][j] = grid[i][j]
    grid = copy.deepcopy(result)
def find_big_ice(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    result = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < 2**n and 0 <= nx < 2**n and not visited[ny][nx] and grid[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
                result += 1
    return result
for i in ls:
    tornado(i)
    melt_ice()
ans, answer = 0, 0
for i in range(2**n):
    for j in range(2**n):
        ans += grid[i][j]
        if grid[i][j] and not visited[i][j]:
            answer = max(answer, find_big_ice(i, j))
print(ans)
print(answer)