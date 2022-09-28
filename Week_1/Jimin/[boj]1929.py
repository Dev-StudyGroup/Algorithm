'''
'소수 구하기'
'''
M, N = map(int, input().split())

a = [False, False] + [True] * (N)
primes = []

for i in range(2, N+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

for i in primes:
    if i <= N and i >= M:
        print(i)