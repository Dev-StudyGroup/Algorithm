#입력
n = int(input())

#출력
for i in range(1, n+1):
    for j in range(n-i, 0, -1):
        print(" ", end='')
    for j in range(i):
        print("*", end='')
    print()
