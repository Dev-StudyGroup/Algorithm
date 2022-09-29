N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)
result = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in range(len(tree)):
        if tree[i]>mid:
            total += tree[i]-mid
    if total < M:
        end = mid - 1
        result = mid

    elif total >= M:
        start = mid + 1

print(end)
