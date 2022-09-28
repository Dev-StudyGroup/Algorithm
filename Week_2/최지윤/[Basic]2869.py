a, b, v = map(int, input().split())
count = 1

v -= a
if v > 0:
    if v % (a - b) == 0:
        count += v // (a - b)
    else:
        count += v // (a - b) + 1

print(count)