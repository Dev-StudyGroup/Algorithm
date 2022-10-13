from collections import defaultdict

import sys
input = sys.stdin.readline

n = int(input().strip())

number_arr = []
number_dict = defaultdict(int)

_sum = 0
_max = -5000
_min = 5000

most_common = [(0, 0)]


for _ in range(n):
    number = int(input().strip())
    number_dict[number] += 1
    number_arr.append(number)

    if most_common[0][1] < number_dict[number]:
        most_common = [(number, number_dict[number])]
    elif most_common[0][1] == number_dict[number]:
        most_common.append((number, number_dict[number]))

    _sum += number
    _max = max(_max, number)
    _min = min(_min, number)

print(round(_sum/n))
print(sorted(number_arr)[n//2])

most_common.sort()

if len(most_common) > 1:
    print(most_common[1][0])
else:
    print(most_common[0][0])

print(_max - _min)
