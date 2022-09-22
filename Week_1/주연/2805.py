n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1, max(arr)

while start <= end:
    mid = (start+end) //2
    print(mid)
    val = 0
    for i in arr:
        if i>= mid:
            val += i-mid
        print(val)

    if val >= m:
        start = mid+1
    else:
        end = mid-1

print(end)