"""
랜선 자르기
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
k, n = map(int, input().split())
lan = []

for i in range(k):
    lan.append(int(input()))

start = 0
end = max(lan)
result = []

while (start <= end):
    count = 0
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    for x in lan:
        count += x // mid
    if count < n:
        end = mid - 1
    else:
        result.append(mid)
        start = mid + 1

print(max(result))
