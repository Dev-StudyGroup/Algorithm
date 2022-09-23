import sys
k, n = map(int, sys.stdin.readline().split())
# k: 이미 가진 랜선의 개수, n: 필요한 랜선의 개수

# for i in range(k):
#     lan.append(int(sys.stdin.readline()))
lan = [int(sys.stdin.readline()) for _ in range(k)]
start = 1; end = max(lan)

while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in lan:
        count += i // mid
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
