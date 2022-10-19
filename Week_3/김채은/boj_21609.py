# [BOJ] 21609 상어 중학교
# Time Taken: 2h 45m

from collections import deque
from typing import final

def find_max_group():

    max_group = []
    max_rainbow_count = -int(1e9)

    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            group, rainbow_count = search_group(i, j, visited)
            max_group_size, group_size = len(max_group), len(group)

            if max_group_size < group_size or (max_group_size == group_size and max_rainbow_count <= rainbow_count):
                max_group_size = group_size
                max_group = group
                max_rainbow_count = rainbow_count

    return max_group

def search_group(i, j, visited):

    group = [(i, j)]
    reference_block = board[i][j]
    rainbow_count = 0

    if reference_block in [BLACK, RAINBOW, EMPTY]: 
        return [], rainbow_count

    dq = deque([(i, j)])
    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]
    visited[i][j] = True
    visited_rainbow_block = []

    while dq:
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
        
            if in_range(ny, nx) and not visited[ny][nx] and board[ny][nx] in [reference_block, RAINBOW]:
                group.append((ny, nx))
                dq.append((ny, nx))
                visited[ny][nx] = True

                if board[ny][nx] == RAINBOW:
                    visited_rainbow_block.append((ny, nx))
                    rainbow_count += 1
    
    for rb in visited_rainbow_block:
        ry, rx = rb
        visited[ry][rx] = False

    if len(group) < 2:
        return [], 0
    else:
        return group, rainbow_count

def in_range(y, x):
    
    if 0 <= y < n and 0 <= x < n:
        return True
    else:
        return False

def remove_group(group):

    score = len(group) ** 2

    for g in group:
        y, x = g

        board[y][x] = EMPTY

    return score

def gravity():

    for i in range(n):
        for j in range(n-2, -1, -1):
            if board[j][i] in [EMPTY, BLACK]:
                continue

            k = j + 1

            while k < n:
                if board[k][i] == EMPTY:
                    board[k][i] = board[k - 1][i]
                    board[k - 1][i] = EMPTY
                else:
                    break

                k += 1

def rotate():
    nboard = [[EMPTY for _ in range(n)] for _ in range(n)]
    for i, j in zip(range(n-1, -1, -1), range(n)):
        for k in range(n):
            nboard[j][k] = board[k][i]

    return nboard


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    EMPTY: final = -2
    BLACK: final = -1
    RAINBOW: final = 0

    score = 0

    while True:
        max_group = find_max_group()

        if len(max_group) == 0:
            break

        score += remove_group(max_group)

        gravity()

        board = rotate()

        gravity()

    print(score)
