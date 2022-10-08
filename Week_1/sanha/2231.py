N = int(input())
flag = False

for i in range(1, N + 1):
    number = list(map(int, str(i)))
    answer = i + sum(number)
    if answer == N:
        print(i)
        flag = True
        break

if not flag:
    print(0)
