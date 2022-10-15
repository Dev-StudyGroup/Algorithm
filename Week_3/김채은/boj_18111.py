from collections import defaultdict
from typing import Final

n, m, b = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(n)]

count_dict = defaultdict(int)

for i in range(n):
    for j in range(m):
        count_dict[ground[i][j]] += 1

INF: Final = int(1e9)

def flat(ref, count, inventory):
    time = 0
    for i, c in count:
        temp = abs(i-ref) * c
        if ref < i:
            time += temp * 2
            inventory += temp
        elif ref > i:
            time += temp
            inventory -= temp

        if inventory < 0:
            return INF
    return time

atime = INF
aheight = -INF

count = sorted(count_dict.items(), key=lambda x:-x[0])

for i in range(257):
    time = flat(i, count, b)
    if atime > time:
        atime, aheight = time, i
    elif atime == time:
        aheight = max(aheight, i)

print(atime, aheight)
