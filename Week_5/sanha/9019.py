from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    q = deque()
    visited = [False] * 10001
    q.append((A, ''))
    while q:
        n, commands = q.popleft()

        if n == B:
            print(commands)
            break

        new_n = (n * 2) % 10000
        if not visited[new_n]:
            q.append((new_n, commands + 'D'))
            visited[new_n] = True

        new_n = (n - 1) % 10000
        if not visited[new_n]:
            q.append((new_n, commands + 'S'))
            visited[new_n] = True

        new_n = ((n * 10) + (n // 1000)) % 10000
        if not visited[new_n]:
            q.append((new_n, commands + 'L'))
            visited[new_n] = True

        new_n = ((n % 10) * 1000 + (n // 10))
        if not visited[new_n]:
            q.append((new_n, commands + 'R'))
            visited[new_n] = True
