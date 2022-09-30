import math

M, N = map(int, input().split())


def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


for n in range(M, N + 1):
    if isPrime(n):
        print(n)
