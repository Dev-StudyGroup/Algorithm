# [BOJ] 1654 랜선 자르기
# Time Taken: 2h

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

left, right = 1, max(lans)

while left <= right:
    mid = (left + right) // 2
    _sum = 0
    for lan in lans:
        _sum += lan // mid

    if _sum >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)