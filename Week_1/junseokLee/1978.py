import math

N = int(input())
arr = list(map(int, input().split()))


def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


count = 0
for n in arr:
    if isPrime(n):
        count += 1

print(count)
