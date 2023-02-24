import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0


def comb(comb_arr, arr, begin, end):
    global result
    if len(arr) == 3:
        result = max(result, sum(arr) + temp[0])
        return
    for i in range(begin, end):
        arr.append(comb_arr[i])
        comb(comb_arr, arr, i + 1, end)
        arr.pop()


def bfs(arr, x, y, visited):
    global result
    if len(arr) == 4:
        result = max(result, sum(arr))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            arr.append(space[nx][ny])
            bfs(arr, nx, ny, visited)
            arr.pop()
            visited[nx][ny] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        space.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            temp = [space[i][j]]
            bfs(temp, i, j, visited)
            visited[i][j] = 0
            comb_array = []
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    comb_array.append(space[nx][ny])
            if len(comb_array) >= 3:
                comb(comb_array, [], 0, len(comb_array))

    print(result)
