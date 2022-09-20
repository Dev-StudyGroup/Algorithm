# 문제
# 마법사 상어가 토네이도를 배웠고, 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.
#
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다. 다음은 N = 7인 경우 토네이도의 이동이다.
#
#
#
# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
#
#
#
# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다. α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다. 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.
#
# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.
#
# 입력
# 첫째 줄에 격자의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
#
# 출력
# 격자의 밖으로 나간 모래의 양을 출력한다.
#
# 제한
# 3 ≤ N ≤ 499
# N은 홀수
# 0 ≤ A[r][c] ≤ 1,000
# 가운데 칸에 있는 모래의 양은 0
import math
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
sy, sx = n//2, n//2
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0
def add_answer(y, x, sand):
    global answer
    if 0 <= y < n and 0 <= x < n:
        grid[y][x] += sand
    else:
        answer += sand
def spread(y, x, ty, tx, d, sand):
    global answer
    one_percent = math.floor(sand*0.01)
    two_percent = math.floor(sand*0.02)
    five_percent = math.floor(sand*0.05)
    seven_percent = math.floor(sand*0.07)
    ten_percent = math.floor(sand*0.1)
    alpha = sand-(2*one_percent)-(2*two_percent)-five_percent-(2*seven_percent)-(2*ten_percent)
    idxs = []
    ny, nx = y+dy[(d+1)%4], x+dx[(d+1)%4]
    idxs.append((ny, nx, one_percent))
    ny, nx = y+dy[(d-1)%4], x+dx[(d-1)%4]
    idxs.append((ny, nx, one_percent))
    ny, nx = ty+2*dy[(d+1)%4], tx+2*dx[(d+1)%4]
    idxs.append((ny, nx, two_percent))
    ny, nx = ty+2*dy[(d-1)%4], tx+2*dx[(d-1)%4]
    idxs.append((ny, nx, two_percent))
    ny, nx = ty+dy[(d+1)%4], tx+dx[(d+1)%4]
    idxs.append((ny, nx, seven_percent))
    ny, nx = ty+dy[(d-1)%4], tx+dx[(d-1)%4]
    idxs.append((ny, nx, seven_percent))
    ny, nx = ty+2*dy[d], tx+2*dx[d]
    idxs.append((ny, nx, five_percent))
    ny, nx = ty+dy[d]+dy[(d+1)%4], tx+dx[d]+dx[(d+1)%4]
    idxs.append((ny, nx, ten_percent))
    ny, nx = ty+dy[d]+dy[(d-1)%4], tx+dx[d]+dx[(d-1)%4]
    idxs.append((ny, nx, ten_percent))
    ny, nx = ty+dy[d], tx+dx[d]
    idxs.append((ny, nx, alpha))
    for cy, cx, cs in idxs:
        add_answer(cy, cx, cs)
cnt, ln, std = 0, 0, 1
d = 2
while (sy, sx) != (0, 0):
    ny, nx = sy+dy[d], sx+dx[d]
    spread(sy, sx, ny, nx, d, grid[ny][nx])
    sy, sx = ny, nx
    cnt += 1
    if cnt == std:
        d = (d-1)%4
        ln += 1
        cnt = 0
        if ln == 2:
            std += 1
            ln = 0
print(answer)