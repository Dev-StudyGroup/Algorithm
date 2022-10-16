dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def move_cloud(clouds, d, s):
    for i in range(len(clouds)):
        clouds[i][0] = (clouds[i][0] + dx[d] * s) % N
        clouds[i][1] = (clouds[i][1] + dy[d] * s) % N
        visited[clouds[i][0]][clouds[i][1]] = 1


def rain():
    for i in range(len(clouds)):
        A[clouds[i][0]][clouds[i][1]] += 1


def remove_cloud():
    return []


def copy_water():
    cross = [1, 3, 5, 7]
    for i in range(len(clouds)):
        count = 0
        for d in cross:
            nx = clouds[i][0] + dx[d]
            ny = clouds[i][1] + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if A[nx][ny] > 0:
                    count += 1
        A[clouds[i][0]][clouds[i][1]] += count  # recheck


def create_cloud():
    clouds_temp = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and not visited[i][j]:
                clouds_temp.append([i, j])
                A[i][j] -= 2
    return clouds_temp


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = []
    res = 0

    for _ in range(N):
        A.append(list(map(int, input().split())))
    clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

    for _ in range(M):
        d, s = map(int, input().split())
        visited = [[0 for _ in range(N)] for _ in range(N)]
        move_cloud(clouds, d - 1, s)
        rain()
        copy_water()
        clouds = remove_cloud()
        clouds = create_cloud()

    for i in range(N):
        res += sum(A[i])
    print(res)
