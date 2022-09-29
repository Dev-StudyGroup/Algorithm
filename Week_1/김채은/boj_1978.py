n = int(input())
numbers = list(map(int, input().split()))
_max = max(numbers)

is_prime = [True for _ in range(_max + 1)]
is_prime[1] = False

for i in range(2, _max // 2 + 1):
    j = 2
    while True:

        if i * j > _max:
            break
        is_prime[i*j] = False

        j += 1

answer = 0

for number in numbers:
    if is_prime[number]:
        answer += 1

print(answer)
