n = int(input())
i = 0; border = 1
while True:
    border += 6 * i
    if n <= border:
        print(i + 1)
        break
    i += 1
