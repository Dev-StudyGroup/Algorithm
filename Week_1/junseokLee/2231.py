N = int(input())
flag = False
for i in range(1, N + 1):
    total = 0
    total += i
    for j in str(i):
        total += int(j)
    if total==N:
        print(i)
        flag = True
        break

if not flag:
    print(0)