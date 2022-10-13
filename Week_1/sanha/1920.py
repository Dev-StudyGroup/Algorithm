N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
numbers2 = list(map(int, input().split()))

numbers.sort()
for number in numbers2:
    if number in numbers:
        print(1)
    else:
        print(0)
