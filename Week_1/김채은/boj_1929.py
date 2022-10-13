# [BOJ] 1929 소수 구하기

m, n = map(int, input().split())

is_prime = [True for _ in range(n+1)]

for i in range(2, n+1):
    j = 2
    while i * j < n + 1:
        is_prime[i * j] = False
        j += 1

for number, value in enumerate(is_prime):
    if max(2, m) <= number <= n and value:
        print(number)
