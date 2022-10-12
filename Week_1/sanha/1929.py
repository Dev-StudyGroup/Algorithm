M, N = map(int, input().split())

def is_even(num):
    if num == 2:
        return True
    if num % 2 == 0 or num == 1:
        return False
    for i in range(3, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(M, N + 1):
    if is_even(i):
        print(i)
