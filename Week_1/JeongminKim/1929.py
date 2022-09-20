"""

    M 이상 N 이하의 소수를 모두 출력

"""

import math
def is_prime_num(num):
    """
    :param num: 소수인지 아닌지 판별할 수
    :return: 소수이면 True, 소수가 아니면, False
    """

    arr = [True] * (num+1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(num)+1)):
        if arr[i]:
            j = 2

            while i * j <= num:
                arr[i*j] = False
                j += 1
    return arr


M, N = map(int, input().split())

prime_net = is_prime_num(N)

for i in range(M, N+1):
    if prime_net[i]:
        print(i)