"""

    1번 ~ N번까지 사람이 원을 이루면서 앉아있다.
    양의 정수
    순서대로 k번째 사람 제거한다.
    한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.

    1번째 방식: dict()
    원형 연결 리스트 형태 사용 ( 이중 연결은 아님 )
"""
table = dict()

N, k = map(int, input().split())
for i in range(1, N + 1):
    if i == N:
        table[i] = 1
    else:
        table[i] = i + 1
table[0] = 1
visited = [0] * (N + 1)
out = []
# k번째 사람
i = 0
# k-1번째 사람
j = 0
cnt = 0
while len(out) != N:

    for _ in range(k):
        j = i
        i = table[i]

    out.append(i)
    table[j] = table[i]
    i = j

print('<', end='')
for i in range(len(out) - 1):
    print(f'{out[i]},', end=' ')
print(f'{out[-1]}>')

