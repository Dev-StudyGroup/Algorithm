from collections import deque
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    q = deque()
    for i in range(len(doc)):
        q.append([i, doc[i]])
    doc.sort(reverse=True)
    count = 0
    while q:
        index, num = q.popleft()
        if num != doc[0]:
            q.append([index, num])
        else:
            doc = doc[1:]
            count += 1
            if index == M:
                break

    print(count)