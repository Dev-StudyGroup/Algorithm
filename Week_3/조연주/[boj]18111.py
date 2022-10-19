"""
마인크래프트
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n, m, b = map(int, input().split())
height = []
top = 0
remove_pull_info = []

for _ in range(n):
    h_list = list(map(int, input().split()))
    top = max(max(h_list), top)
    height.append(h_list)

for t in range(0, top + 1):
    remove, pull = 0, 0
    for i in range(n):
        for j in range(m):
            if height[i][j] == t:
                continue
            elif height[i][j] < t:
                pull += (t - height[i][j])
            else:
                remove += (height[i][j] - t)
    
    remove_pull_info.append((remove, pull))

time = 99999999
ground = -1

for i in range(len(remove_pull_info)):
    r, p = remove_pull_info[i]
    if p <= r + b:
        t = (r * 2) + (p * 1)
        time = min(time, t)
        if time == t:
            ground = i

print(time, ground)
