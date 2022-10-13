import sys

input = sys.stdin.readline

n = int(input().strip())

numbers = []

for _ in range(n):
    numbers.append(int(input().strip()))

numbers.sort()

for number in numbers:
    print(number)
