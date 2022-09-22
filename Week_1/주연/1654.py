n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
start, end = 1, max(arr)

while start <= end:
    mid = (start+end) // 2
    val = 0
    for i in arr:
        val += i //mid

    if val >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)