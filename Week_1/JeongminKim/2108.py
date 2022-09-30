"""

    N개의 수들로 이루어진 수들의 집합 A은 홀수로 이루어짐
    1. 산술평균: sum(A) / N
    2. 중앙값: 오름차순으로 나열하였을 떄, A[N//2]
    3. 최빈값: A중 가장 많이 나타나는 값
    4. 범위: Max(A) - Min(A)

"""
from collections import Counter
import sys

N = int(input())
A = []

for _ in range(N):
    A.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(A)/N))

# 중앙값
A = sorted(A)
print(A[N//2])


# 최빈값
modes = Counter(A).most_common()
if len(modes) > 1:
    if modes[0][1] == modes[1][1]:
        modes = modes[1][0]
    else:
        modes = modes[0][0]
else:
    modes = modes[0][0]
print(modes)
# 범위 계산
print(A[-1]-A[0])

