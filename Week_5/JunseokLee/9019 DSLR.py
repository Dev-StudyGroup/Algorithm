import sys
from collections import deque


def bfs(q, des, visited):
    while q:
        num, ans = q.popleft()
        if num == des:
            return ans
        D = (num * 2) % 10000
        S = (num - 1) % 10000
        L = (num % 1000) * 10 + num // 1000
        R = (num % 10) * 1000 + (num // 10)
        if not visited[D]:
            visited[D] = 1
            q.append((D, ans + 'D'))
        if not visited[S] and 0 <= S < 10000:
            visited[S] = 1
            q.append((S, ans + 'S'))
        if not visited[L]:
            visited[L] = 1
            q.append((L, ans + 'L'))
        if not visited[R]:
            visited[R] = 1
            q.append((R, ans + 'R'))


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        visited = [0] * 10001
        queue = deque()
        queue.append((A, ""))
        print(bfs(queue, B, visited))
