import math

a, b, v = map(int, input().split())

print(int(math.ceil((v - a) / (a - b))) + 1)
