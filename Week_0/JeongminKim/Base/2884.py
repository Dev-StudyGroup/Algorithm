h, m = map(int, input().split())

if h == 0:
    if m < 45:
        h = 23
        m = m + 60 - 45
    else:
        m = m - 45

else:
    if m < 45:
        h -= 1
        m = m + 60 - 45
    else:
        m = m - 45

print(h, m)