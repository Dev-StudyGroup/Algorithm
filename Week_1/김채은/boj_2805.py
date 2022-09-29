# [BOJ] 2805 나무자르기
# Time Tiken: 18m

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def cut(height):
    cut_length = 0
    for tree in trees:
        if tree > height:
            cut_length += tree - height
    return cut_length

left, right = 0, max(trees) - 1

while left <= right:   

    mid = (left + right) // 2

    cut_length = cut(mid)

    if cut_length >= m:
        left = mid + 1
    elif cut_length < m:
        right = mid - 1

print(right)
