# 문제
# 상어 중학교의 코딩 동아리에서 게임을 만들었다. 이 게임은 크기가 N×N인 격자에서 진행되고, 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다. 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 검은색 블록은 -1, 무지개 블록은 0으로 표현한다. (i, j)는 격자의 i번 행, j번 열을 의미하고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2)를 인접한 칸이라고 한다.
#
# 블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
#
# 오늘은 이 게임에 오토 플레이 기능을 만드려고 한다. 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복되어야 한다.
#
# 크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
# 1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
# 격자에 중력이 작용한다.
# 격자가 90도 반시계 방향으로 회전한다.
# 다시 격자에 중력이 작용한다.
# 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
#
# 다음은 N = 5, M = 3인 경우의 예시이다.
#
# 여기서 찾을 수 있는 크기가 가장 큰 블록 그룹을 다음과 같이 빨간색으로 표시했다.
#
# 블록 그룹이 제거되면 다음과 같이 변하고, 점수 82점을 획득한다.
#
# 중력이 작용하면 다음과 같이 변한다.
#
# 90도 반시계방향으로 회전한 결과는 다음과 같다.
#
# 다시 여기서 중력이 작용하면 다음과 같이 변한다.
#
# 오토 플레이가 모두 끝났을 때 획득한 점수의 합을 구해보자.
#
# 입력
# 첫째 줄에 격자 한 변의 크기 N, 색상의 개수 M이 주어진다.
#
# 둘째 줄부터 N개의 줄에 격자의 칸에 들어있는 블록의 정보가 1번 행부터 N번 행까지 순서대로 주어진다. 각 행에 대한 정보는 1열부터 N열까지 순서대로 주어진다. 입력으로 주어지는 칸의 정보는 -1, 0, M이하의 자연수로만 이루어져 있다.
#
# 출력
# 첫째 줄에 획득한 점수의 합을 출력한다.
#
# 제한
# 1 ≤ N ≤ 20
# 1 ≤ M ≤ 5
from collections import deque
import copy
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0 ,1, 0, -1], [1, 0, -1, 0]
answer = 0
def find_group(sy, sx):
    q = deque()
    q.append((sy, sx))
    std = grid[sy][sx]
    visited[sy][sx] = True
    path = [(sy, sx)]
    rainbows = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if grid[ny][nx] == 0 and (ny, nx) not in set(path):
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    path.append((ny, nx))
                    rainbows += 1
                if grid[ny][nx] == std and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    path.append((ny, nx))
    return (rainbows, path)
def remove_group(group):
    global answer
    for y, x in group:
        grid[y][x] = -2
    answer += len(group)**2
def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if grid[i][j] > -1:
                r = i
                while True:
                    if 0 <= r+1 < n and grid[r+1][j] == -2:
                        grid[r+1][j] = grid[r][j]
                        grid[r][j] = -2
                        r += 1
                    else:
                        break
def rotate():
    global grid
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = grid[j][n-1-i]
    grid = copy.deepcopy(tmp)
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    groups = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0 and not visited[i][j]:
                group = find_group(i, j)
                if len(group[1]) >= 2:
                    groups.append((group[0], group[1], i, j))
    if groups:
        remove_group(sorted(groups, key=lambda x:(len(x[1]), x[0], x[2], x[3]), reverse=True)[0][1])
        gravity()
        rotate()
        gravity()
    else:
        break
print(answer)
