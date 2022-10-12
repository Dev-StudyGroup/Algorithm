N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
start = 1
end = max(trees)
Max = 0

while start <= end:
    mid = (start + end) // 2
    height = 0
    cut = 0
    for tree in trees:
        cut = tree - mid
        if cut < 0:
            cut = 0
        height += cut
    if height >= M:
        Max = max(Max, mid)
    if height <= M:
        end = mid - 1
    else:
        start = mid + 1

print(Max)
