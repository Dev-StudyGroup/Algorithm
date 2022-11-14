"""

    지렁이가 이동하는 방향

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    지렁이는 땅 밖으로 못 나간다. => 땅 밖인지 아닌지 return 해주는 함수
    visited = [[][]] 땅의 크기만큼 생성
    dx, dy의 방향을 차례대로 순회하면서, 배추가 있는 땅을 방문.

"""
from collections import deque


def is_on_the_ground(xi, yi):
    """ 지렁이가 밭 안에 있는 것을 확인"""
    # 배추밭의 크기를 global로 불러오기
    global M, N

    if 0 <= xi < M and 0 <= yi < N:
        return True
    else:
        return False


def is_visited(xi, yi):
    """지렁이가 배추가 있는 xi, yi 배추밭에 방문하였을 때 방문하였는지(True) 안했는지(False) 리턴"""
    global visited

    if not visited[xi][yi]:
        return False
    else:
        return True


def is_cabbage(xi, yi):
    """ 배추가 있는 지 없는 지 리턴 """
    global ground

    if ground[xi][yi]:
        return True
    else:
        return False


def bfs(xi, yi):
    global visited, ground
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cabbage_list = deque()
    cabbage_list.append([xi, yi])

    while cabbage_list:
        temp_x, temp_y = cabbage_list.popleft()
        if is_visited(temp_x, temp_y):
            continue
        visited[temp_x][temp_y] = 1
        for idx, idy in zip(dx, dy):
            next_x = temp_x + idx
            next_y = temp_y + idy
            if is_on_the_ground(next_x, next_y):
                if is_cabbage(next_x, next_y) and not is_visited(next_x, next_y):
                    cabbage_list.append([next_x, next_y])


if __name__ == '__main__':
    import sys

    T = int(input())
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        ground = [[0] * N for _ in range(M)]
        visited = [[0] * N for _ in range(M)]
        for _ in range(K):
            x_a, y_a = map(int, sys.stdin.readline().split())
            ground[x_a][y_a] = 1
        worm = 0
        for i in range(M):
            for j in range(N):
                if is_cabbage(i, j) and not is_visited(i, j):
                    bfs(i, j)
                    worm += 1
        print(worm)