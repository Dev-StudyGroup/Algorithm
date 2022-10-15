n, k = map(int, input().split())

n_fac, nmk_fac, k_fac = 1, 1, 1

for i in range(2, n + 1):
    n_fac *= i

for i in range(2, n - k + 1):
    nmk_fac *= i

for i in range(2, k + 1):
    k_fac *= i

print(n_fac // (nmk_fac*k_fac))
