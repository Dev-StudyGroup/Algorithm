T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    flag = False

    while x <= M * N:
        if (x - y) % N == 0:
            print(x)
            flag = True
            break
        x += M

    if not flag:
        print(-1)
