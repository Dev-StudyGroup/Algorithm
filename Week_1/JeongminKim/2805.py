"""

    M미터가 필요

    1. 절단기 높이 H를 지정
    2. 톱날이 땅으로 부터 H미터 위로 이동
    3. 한 줄에 연속해 있는 나무를 모두 절단
        + 따라서 높이가 H보다 큰 나무는 H위의 부분이 잘리고
        + 낮은 나무는 잘리지 않을 것이다.
    4. 상근이는 그럼 잘린 나무를 가지고 가져간다.
    5. 필요한 만큼만 가져간다.
    6. 절단기에 설정할 수 있는 높이의 최댓값 산출
    
    이분탐색

"""
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

h = 0
sum_blocks = 0
max_h = max(trees)
min_h = 0


while min_h <= max_h:
    sum_blocks = 0
    mid_h = (min_h + max_h) // 2
    for tree in trees:
        if tree > mid_h:
            sum_blocks += (tree-mid_h)
    if sum_blocks >= M:
        min_h = mid_h+1
    else:
        max_h = mid_h-1


print(max_h)