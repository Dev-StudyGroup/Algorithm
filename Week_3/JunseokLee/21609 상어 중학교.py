from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))


def find_block():
    q = deque()
    blocks = []
    rainbow = -1
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if space[i][j] == 0:
                visited[i][j] = []
    for i in range(N):
        for j in range(N):
            if space[i][j] > 0:
                num = space[i][j]
                q.append([i, j])
                visited[i][j] = num
                temp = []
                rainbow_cnt = 0

                while q:
                    x, y = q.popleft()
                    temp.append([x, y])
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            if space[nx][ny] == num and not visited[nx][ny]:
                                visited[nx][ny] = num
                                q.append([nx, ny])
                            elif space[nx][ny] == 0 and (num not in visited[nx][ny]):
                                rainbow_cnt += 1
                                visited[nx][ny].append(num)
                                q.append([nx, ny])
                if len(blocks) < len(temp):
                    blocks = temp
                elif len(blocks) == len(temp):
                    if rainbow > rainbow_cnt:
                        continue
                    elif rainbow < rainbow_cnt:
                        rainbow = rainbow_cnt
                        blocks = temp
                    else:
                        if blocks[0][0] < temp[0][0]:
                            blocks = temp
                        elif blocks[0][0] == temp[0][0]:
                            if blocks[0][1] < temp[0][1]:
                                blocks = temp
    return blocks


def remove_block(blocks):
    for x, y in blocks:
        space[x][y] = -2


def gravity():
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if space[i][j] < 0:
                continue
            idx = i
            while idx < N - 1 and space[idx + 1][j] == -2:
                idx += 1
            if idx != i:
                space[i][j], space[idx][j] = space[idx][j], space[i][j]


def reverse_rotate_90_degree():
    global space
    space = list(map(list, zip(*space)))[::-1]


if __name__ == "__main__":
    res = 0
    while True:
        blocks = find_block()
        block_length = len(blocks)
        if block_length < 2:
            break
        else:
            res += block_length * block_length
        print(block_length*block_length, blocks[0][0],blocks[0][1])
        remove_block(blocks)
        gravity()
        reverse_rotate_90_degree()
        gravity()
        for i in range(N):
            for j in range(N):
                print(space[i][j], end=' ')
            print()
        print("=======================")
    print(res)
