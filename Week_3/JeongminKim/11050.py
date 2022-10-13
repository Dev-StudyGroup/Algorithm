"""

    이항계수 구하기

"""

n, k = map(int, input().split())

if k > n // 2:
    k = n - k
u = 1
d = 1
for i in range(n, n - k, -1):
    u *= i
for j in range(k, 0, -1):
    d *= j

print(int(u / d))
