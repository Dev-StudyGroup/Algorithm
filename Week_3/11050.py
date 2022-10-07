"""
11050: 이항 계수1
"""
from itertools import combinations

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, k = map(int, input().split()) # nCk 값을 구하면 된다.

# ver 1
ans = combinations(range(n), k)
result=0
for i in ans:
    result += 1
print(result)

# ver 2
result = fac(n) / (fac(n - k) * fac(k))
print(int(result))

