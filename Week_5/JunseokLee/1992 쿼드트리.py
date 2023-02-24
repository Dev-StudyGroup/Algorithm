import sys

input = sys.stdin.readline


def divide(x, y, n):
    global result
    num = space[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if space[i][j] != num:
                result += '('
                for k in range(2):
                    for l in range(2):
                        divide(x + k * n // 2, y + l * n // 2, n // 2)
                result += ')'
                return
    result += str(num)


if __name__ == "__main__":
    N = int(input())
    space = []
    result = ''
    for _ in range(N):
        space.append(list(map(int, ' '.join(input()).split())))
    divide(0, 0, N)
    print(result)
