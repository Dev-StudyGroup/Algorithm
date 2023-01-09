import sys
from collections import deque

input = sys.stdin.readline


def move_shark(space, fish):
    global time, baby_shark_position
    time += fish[2]
    space[baby_shark_position[0]][baby_shark_position[1]] = 0
    baby_shark_position = [fish[0], fish[1]]
    space[fish[0]][fish[1]] = 9


def check_eatable(space, baby_size):
    global eatable, baby_shark_position, time
    eatable = []
    x, y = baby_shark_position[0], baby_shark_position[1]
    q = deque([[x, y]])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and space[nx][ny] <= baby_size and visited[nx][ny] < 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                if 0 < space[nx][ny] < baby_size:
                    eatable.append([nx, ny, visited[nx][ny]])

    eatable_count = len(eatable)
    if eatable_count == 0:
        return False

    elif eatable_count == 1:
        move_shark(space, eatable[0])

    elif eatable_count > 1:
        eatable.sort(key=lambda x: (x[2], x[0], x[1]))
        move_shark(space, eatable[0])

    return True


if __name__ == "__main__":
    baby_shark_position = [0, 0]
    baby_shark_size = 2
    eat_count = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    eatable = []
    time = 0
    N = int(input())
    space = []
    for n in range(N):
        array = list(map(int, input().split()))
        space.append(array)

    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                baby_shark_position = [i, j]

    while True:
        if not check_eatable(space, baby_shark_size):
            break
        eat_count += 1
        if eat_count == baby_shark_size:
            baby_shark_size += 1
            eat_count = 0

    print(time)
