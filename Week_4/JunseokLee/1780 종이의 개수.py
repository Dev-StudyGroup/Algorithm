def check(x, y, n):
    num = space[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if space[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        check(x + k * n // 3, y + l * n // 3, n // 3)
                return
    count[num + 1] += 1


if __name__ == "__main__":
    N = int(input())
    space = []
    count = [0, 0, 0]
    for _ in range(N):
        space.append(list(map(int, input().split())))

    check(0, 0, N)

    for cnt in count:
        print(cnt)
