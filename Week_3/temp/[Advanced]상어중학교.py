from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, value, visited, visited_now):
    global count_block, count_rainbow

    visited_now[x][y] = 1
    if board[x][y] > 0:
        visited[x][y] = 1
    count_block += 1
    count_rainbow += 1 if board[x][y] == 0 else 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or visited_now[nx][ny]:
            continue
        if board[nx][ny] == value or board[nx][ny] == 0: 
            dfs(nx, ny, value, visited, visited_now)
        

def findMaxBlockGroup():
    global count_block, count_rainbow
    max_block_group = (0, 0, 0, 0)
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j]:
                visited_now = [[0]*n for _ in range(n)]
                count_block, count_rainbow = 0, 0

                dfs(i, j, board[i][j], visited, visited_now)
                if count_block >= 2:
                    max_block_group = max(max_block_group, (count_block, count_rainbow, i, j))

    return max_block_group


def removeBlockGroup(x, y):
    queue = deque()
    visited = [[0]*n for _ in range(n)]
    queue.append((x, y))
    value = board[x][y]
    board[x][y] = -2

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if board[nx][ny] == value or board[nx][ny] == 0:
                queue.append((nx, ny))
                board[nx][ny] = -2


def gravity():
    for j in range(n):
        remained = []
        for i in range(n-1, -1, -1):
            if board[i][j] == -1:
                remained = remained + [-2] * (n - i - len(remained) - 1)
            if board[i][j] != -2:
                remained.append(board[i][j])

        remained = remained + [-2] * (n - len(remained))
        for i in range(n-1, -1, -1):
            board[i][j] = remained[n-i-1]


def rotateCounterclockwise():
    return list(map(list, zip(*board)))[::-1]


result = 0
while 1:
    block_size, _, standard_x, standard_y = findMaxBlockGroup()
    if block_size == 0:
        break

    removeBlockGroup(standard_x, standard_y)
    result += block_size**2

    gravity()

    board = rotateCounterclockwise()

    gravity()

print(result)