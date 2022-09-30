'''
'최소, 최대'
'''
N = int(input())
num_list = list(map(int, input().split()))

# print(min(num_list), max(num_list))

maximum = -1000001
minimum = 1000001

for i in num_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(minimum, maximum)