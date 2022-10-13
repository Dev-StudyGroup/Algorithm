N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for number in numbers:
    print(number)
