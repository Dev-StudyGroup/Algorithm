n = int(input())

result = 0
while 0 < n:
    if n % 5 == 0:
        n -= 5
    elif n % 3 == 0:
        n -= 3
    else:
        n -= 5
    result += 1

if n < 0:
    print(-1)
else:
    print(result)