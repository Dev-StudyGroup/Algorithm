"""
소수 구하기
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
m, n = map(int, input().split())
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

for i in range(len(primes)):
    if primes[i] < m:
        continue
    else:
        print(primes[i])
