import sys

input = sys.stdin.readline
colors = [0, 0]


def divide(array, x, y, n):
    if check(array, x, y, n):
        colors[array[x][y]] += 1
        return
    divide(array, x, y, n // 2)
    divide(array, x + n // 2, y, n // 2)
    divide(array, x, y + n // 2, n // 2)
    divide(array, x + n // 2, y + n // 2, n // 2)


def check(array, x, y, n):
    num = array[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if array[i][j] != num:
                return False
    return True


if __name__ == "__main__":
    N = int(input())
    space = []
    for i in range(N):
        space.append(list(map(int, input().split())))
    divide(space, 0, 0, N)
    for color in colors:
        print(color)
