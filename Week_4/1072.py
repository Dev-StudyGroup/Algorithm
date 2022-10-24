"""
1012: 유기농 배추

전체 탐색을 사용한다면 너무 많은 연산이 필요하기 때문에
필요한 곳만 탐색하고 나머지는 빠르게 넘기는 분할탐색 알고리즘을 사용해야 한다.
"""

N, r, c = map(int, input().split())
count = 0

while N > 1:
    size = (2 ** N) // 2 # 1
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        count += size ** 2 # 1
        c -= size
    elif r >= size and c < size:
        count += size ** 2 * 2 # 2
        r -= size
    elif r >= size and c >= size:
        count += size ** 2 * 2 * 3 # 3
        c -= size
        r -= size
    N -= 1

if r == 0 and c == 0:
    print(count)
if r == 0 and c == 1:
    print(count + 1)
if r == 1 and c == 0:
    print(count + 2)
if r == 1 and c == 1:
    print(count + 3)

    