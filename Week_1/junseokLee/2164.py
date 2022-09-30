from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])
if len(q) == 1:
    print(q.popleft())
else:
    while q:
        q.popleft()
        q.append(q.popleft())
        if len(q) == 1:
            print(q.popleft())
            break
