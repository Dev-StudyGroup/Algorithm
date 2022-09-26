"""
프린터 큐
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    level = list(map(int, input().split()))
    now = m
    cnt = 0

    while level:
        best = max(level)
        if level[0] != best:
            level.append(level.pop(0))
            if now == 0:
                now = len(level) - 1
            else:
                now -= 1
        else:
            level.pop(0)
            cnt += 1
            if now == 0:
                print(cnt)
                break
            now -= 1
