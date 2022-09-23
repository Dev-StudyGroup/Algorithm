# 정해진 길이들 내에서 최대, 최솟값을 구해야 하면 이진탐색 사용하기
import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1; end = max(trees); 
while start <= end:
    wood = 0
    mid = (start + end) // 2
    for i in trees:
        # if i - mid < 0:
        #     wood += 0
        # else:
        #     wood += i - mid
        if i >= mid:
            wood += i - mid
        # 불필요한 연산 줄이기!
    if wood >= m:
        start = mid + 1
    else: # wood < m
        end = mid - 1
print(end)