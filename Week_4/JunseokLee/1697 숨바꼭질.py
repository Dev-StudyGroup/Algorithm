from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    result = 0
    q = deque()
    visited = [0] * (100001)
    q.append([N, 0])
    while q:
        num, cnt = q.popleft()
        if num == K:
            result = cnt
            break
        a, b, c = num - 1, num + 1, num * 2
        if a > -1 and not visited[a]:
            visited[a] = 1
            q.append([a, cnt + 1])
        if b < 100001 and not visited[b]:
            visited[b] = 1
            q.append([b, cnt + 1])
        if c < 100001 and not visited[c]:
            visited[c] = 1
            q.append([c, cnt + 1])
    print(result)
