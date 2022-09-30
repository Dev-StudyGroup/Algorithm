'''
'나무 자르기'
'''
from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = Counter(map(int, input().split())).items()

start = 1
end = max(tree)[0]

answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in tree:
        if i[0] - mid > 0:
            cnt += (i[0] - mid) * i[1]

    if cnt < M:
        end = mid - 1
    elif cnt >= M:
        answer = mid
        start = mid + 1

print(answer)