from collections import deque

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    priority = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        Max = max(priority)
        cur = priority.popleft()
        M -= 1
        if Max == cur:
            if M < 0:
                print(cnt)
                break
            cnt += 1
        else:
            priority.append(cur)
            if M < 0:
                M = len(priority) - 1
