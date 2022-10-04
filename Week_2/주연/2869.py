a, b, v = map(int, input().split())
snail = 0
day = 0
while snail != v:
    day += 1
    if snail != v:
        snail += a
    else: break
    if snail != v:
        snail -= b
    else: break

print(day)