"""

    입력 값
    랜선의 개수 K
    필요한 랜선의 개수 N

    주어진 랜선중에서 가장 작은 랜선보다 작은 길이를 가져야한다.

"""

K, N = map(int, input().split())
lines = []
for _ in range(0, K):
    lines.append(int(input()))

end = max(lines)
start = 1

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)