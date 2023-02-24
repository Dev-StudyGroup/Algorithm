def cut(n, y, x):
    size = n//3

    for i in range(3):
        for j in range(3):
            number = check_fill(size, y + size * i, x + size * j)

            if number != -2:
                answer[str(number)] += 1
            else:
                cut(size, y + size * i, x + size * j)

def check_fill(size, y, x):
    number = matrix[y][x]

    for i in range(size):
        for j in range(size):
            if number != matrix[y + i][x + j]:
                return -2

    return number


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    answer = { '-1': 0, '0': 0, '1':0 }

    origin = check_fill(n, 0, 0)
    if origin != -2:
        answer[str(origin)] += 1
    else:
        cut(n, 0, 0)

    for a in answer.values():
        print(a)