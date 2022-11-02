'''
'마법사 상어와 비바라기'
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move(x, y, d, s):
    mx = (x + (dx[d-1] * s)) % N
    my = (y + (dy[d-1] * s)) % N
    return mx, my

def magic(x, y):
    result = 0
    for i in range(1, 8, 2):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx >= N or my < 0 or my >= N:
            continue
        else:
            if board[mx][my] >= 1:
                result += 1
    return result

for i in range(M):
    d, s = map(int, input().split())
    for j in range(len(cloud)):
        x, y = cloud[j]
        x, y = move(x, y, d, s)
        cloud[j] = [x, y]
        board[x][y] += 1

    for j in range(len(cloud)):
        x, y = cloud[j]
        temp = magic(x, y)
        board[x][y] += temp

    new_cloud = []
    cloud.sort()                            # for문으로 일일히 cloud에 [j, k]가 있는지 비교하면 시간복잡도가 늘어나기 때문에 정렬
    for j in range(N):
        for k in range(N):
            if len(cloud) != 0:
                if [j, k] == cloud[0]:      # cloud를 정렬했기 때문에 맨앞 구름만 비교
                    cloud.pop(0)
                    continue
            if board[j][k] >= 2:
                new_cloud.append([j, k])
                board[j][k] -= 2

    cloud = new_cloud

answer = 0
for i in range(N):
    answer += sum(board[i])

print(answer)
