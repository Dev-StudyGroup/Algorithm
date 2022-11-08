import sys
input = sys.stdin.readline

n = int(input().strip())

numbers = [0 for _ in range(10001)]

for _ in range(n):
    number = int(input().strip())
    numbers[number] += 1

for i in range(1, 10001):
    for _ in range(numbers[i]):
        print(i)