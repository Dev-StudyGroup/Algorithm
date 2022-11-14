"""

    N * N
    1 <= N <= 3 ** 7
    N = 3 ** K 꼴로 주어짐

    종이의 각 칸엔 -1, 0, 1로 저장되어있음

    1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용
    2. (1)이 아닌 경우 종이를 같은 크기의 종이 9개로 자른다.

    N = 3 ** K
    K = 3
    3 ** (k-1) = 9
    range(0, 28, 9) => 0, 9, 18, 27
    0 ~ 8 [:9]
    9 ~ 17 [9:18]
    18 ~ 26 [18: ]

    range(0, 2**K, 2**K-1)

"""


def dfs(array, x, y, size):
    array_num = array[x][y]
    global result_minus, result_zero, result_plus

    for i in range(x, x + size):
        for j in range(y, y + size):
            if array_num != array[i][j]:
                for n_x in range(x, x+size, size//3):
                    for n_y in range(y, y+size, size//3):
                        dfs(array, n_x, n_y, size // 3)
                return

    if array_num == -1:
        result_minus += 1
    if array_num == 0:
        result_zero += 1
    if array_num == 1:
        result_plus += 1


if __name__ == '__main__':

    result_minus = 0
    result_zero = 0
    result_plus = 0
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    dfs(arr, 0, 0, N)
    result = [result_minus, result_zero, result_plus]
    print('\n'.join(list(map(str, result))))
