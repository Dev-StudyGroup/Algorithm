n = int(input())

i = 1
start = 1
while start < n:
    start += 6 * i
    i += 1

print(i)
