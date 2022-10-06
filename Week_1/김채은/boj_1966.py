from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    imp_count = [0 for _ in range(10)]

    for imp in importance:
        imp_count[imp] += 1

    dq = deque(importance)

    def is_important(head):
        for i in range(head+1, 10):
            if imp_count[i]:
                return False
        return True

    count = 0
    while dq:
        head = dq[0]
        if is_important(head):
            imp_count[dq.popleft()] -= 1
            count += 1
            if m == 0:
                break
            else:
                m -= 1
        else:
            dq.append(dq.popleft())
            if m == 0:
                m = len(dq) - 1
            else:
                m -= 1

    print(count)
