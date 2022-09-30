def isPrime(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                return False
        return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)
