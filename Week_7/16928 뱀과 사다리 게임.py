import sys
from collections import deque

input = sys.stdin.readline


def move(now, number):
    now += number
    for i in range(len(ladders)):
        if now == ladders[i][0]:
            now = ladders[i][1]
            break

    for j in range(len(snakes)):
        if now == snakes[j][0]:
            now = snakes[j][1]
            break

    return now


if __name__ == "__main__":
    N, M = map(int, input().split())
    ladders = []
    snakes = []
    visited = [0] * 101
    for _ in range(N):
        x, y = map(int, input().split())
        ladders.append([x, y])
    for _ in range(M):
        u, v = map(int, input().split())
        snakes.append([u, v])

    q = deque([1])

    while q:
        now = q.popleft()
        for i in range(1, 7):
            temp = now + i
            if temp > 100:
                continue

            if not visited[temp]:
                visited[temp] = visited[now] + 1
                next_move = move(now, i)
                if next_move != temp and not visited[next_move]:
                    visited[next_move] = visited[temp]
                q.append(next_move)
    print(visited[100])
