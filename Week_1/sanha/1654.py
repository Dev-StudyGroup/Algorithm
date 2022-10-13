K, N = map(int, input().split())
numbers = list(int(input()) for _ in range(K))
start = 1
end = max(numbers)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for number in numbers:
        cnt += number // mid
    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)
