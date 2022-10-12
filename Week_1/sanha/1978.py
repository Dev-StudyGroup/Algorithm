N = int(input())
numbers = list(map(int, input().split()))
cnt = 0

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number == 1:
        return False
    for i in range(3, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

for number in numbers:
    if is_prime(number):
        cnt += 1

print(cnt)
