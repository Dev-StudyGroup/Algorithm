# 문제
# 마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그, 비바라기 마법을 할 수 있다. 오늘 새로 배운 마법은 블리자드이고, 크기가 N×N인 격자에서 연습하려고 한다. N은 항상 홀수이고, (r, c)는 격자의 r행 c열을 의미한다. 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이며 마법사 상어는 ((N+1)/2, (N+1)/2)에 있다.
#
# 일부 칸과 칸 사이에는 벽이 세워져 있으며, 다음은 N = 3, 5, 7인 경우의 예시이다. 실선은 벽이고, 점선은 벽이 아니다. 칸에 적혀있는 수는 칸의 번호이다.
#
# 가장 처음에 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다. 구슬은 1번 구슬, 2번 구슬, 3번 구슬이 있다. 같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬이라고 한다. 다음은 N = 7인 경우 예시이다.
#
# 블리자드 마법을 시전하려면 방향 di와 거리 si를 정해야 한다. 총 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4로 나타낸다. 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다. 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다. 얼음 파편은 벽의 위로 떨어지기 때문에, 벽은 파괴되지 않는다.
#
# 다음 예시는 방향은 아래, 거리는 2인 경우이다.
#
# 만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다. 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복된다. 따라서, 구슬이 파괴된 후에는 빈 칸이 생겨 구슬이 이동하고, 구슬이 모두 이동한 결과는 다음과 같다.
#
# 이제 구슬이 폭발하는 단계이다. 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생한다. 다음은 왼쪽 그림은 위의 상태에서 폭발하는 구슬이 들어있는 칸을 파란색과 초록색으로 표시한 것이고, 오른쪽 그림은 구슬이 폭발한 후의 상태이다.
#
# 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동한다. 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계이고, 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복된다. 구슬이 폭발한 후의 상태에서 구슬이 이동하면 다음과 같다.
#
# 위의 상태는 4개 이상 연속하는 구슬이 있기 때문에 구슬이 다시 폭발하게 된다.
#
# 이제 더 이상 폭발한 구슬이 없기 때문에, 구슬이 변화하는 단계가 된다. 연속하는 구슬은 하나의 그룹이라고 한다. 다음은 1번 구슬은 빨간색, 2번 구슬은 파란색, 3번 구슬은 보라색으로 표시한 그림이다.
#
# 하나의 그룹은 두 개의 구슬 A와 B로 변한다. 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호이다. 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다. 다음 그림은 구슬이 변화한 후이고, 색은 구분하기 위해 위의 그림에 있는 그룹의 색을 그대로 사용했다. 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
#
# 마법사 상어는 블리자드를 총 M번 시전했다. 시전한 마법의 정보가 주어졌을 때, 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)를 구해보자.
#
# 입력
# 첫째 줄에 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 격자에 들어있는 구슬의 정보가 주어진다. r번째 행의 c번째 정수는 (r, c)에 들어있는 구슬의 번호를 의미한다. 어떤 칸에 구슬이 없으면 0이 주어진다. 상어가 있는 칸도 항상 0이 주어진다.
#
# 다음 M개의 줄에는 블리자드 마법의 방향 di와 거리 si가 한 줄에 하나씩 마법을 시전한 순서대로 주어진다.
#
# 출력
# 첫째 줄에 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)를 출력한다.
#
# 제한
# 3 ≤ N ≤ 49
# N은 홀수
# 1 ≤ M ≤ 100
# 1 ≤ di ≤ 4
# 1 ≤ si ≤ (N-1)/2
# 칸에 들어있는 구슬이 K개라면, 구슬이 들어있는 칸의 번호는 1번부터 K번까지이다.
# 입력으로 주어진 격자에는 4개 이상 연속하는 구슬이 없다.
import copy
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
shark = [n//2, n//2]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
commands = [list(map(int, input().split())) for _ in range(m)]
path = [(shark[0], shark[1])]
answer = 0
def make_path():
    mapping = [2, 3, 1, 0]
    cnt, std, std_cnt = 0, 1, 0
    cy, cx = shark
    d = 2
    while True:
        if cy == 0 and cx == 0:
            break
        cy, cx = cy+dy[d], cx+dx[d]
        path.append((cy, cx))
        cnt += 1
        if cnt == std:
            d = mapping[d]
            std_cnt += 1
            cnt = 0
            if std_cnt == 2:
                std += 1
                std_cnt = 0
def blizzard(d, s):
    d -= 1
    for i in range(1, s+1):
        ny, nx = shark[0]+i*dy[d], shark[1]+i*dx[d]
        if 0 <= ny < n and 0 <= nx < n:
            grid[ny][nx] = 0
def move_marbles():
    global grid
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    idx = 1
    for i in range(len(path)):
        y, x = path[i]
        if grid[y][x]:
            new_grid[path[idx][0]][path[idx][1]] = grid[y][x]
            idx += 1
    grid = copy.deepcopy(new_grid)
def marble_bomb():
    global answer
    start, std = 0, 0
    for i in range(len(path)):
        y, x = path[i]
        if grid[y][x] != std:
            if i-start >= 4:
                answer += (i-start)*std
                for j in range(start, i):
                    r, c = path[j]
                    grid[r][c] = 0
            start = i
            std = grid[y][x]
def change_marbles():
    global grid
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    start, std, idx = 1, grid[path[1][0]][path[1][1]], 1
    for i in range(1, len(path)):
        y, x = path[i]
        if grid[y][x] != std:
            new_grid[path[idx][0]][path[idx][1]] = i-start
            idx += 1
            if idx >= len(path):
                break
            new_grid[path[idx][0]][path[idx][1]] = std
            idx += 1
            if idx > len(path)-1:
                break
            start = i
            std = grid[y][x]
    grid = copy.deepcopy(new_grid)
make_path()
for d, s in commands:
    blizzard(d, s)
    move_marbles()
    while True:
        tmp = 0+answer
        marble_bomb()
        move_marbles()
        if tmp == answer:
            break
    change_marbles()
print(answer)
