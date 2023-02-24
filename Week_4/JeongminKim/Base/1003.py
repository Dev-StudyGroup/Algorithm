"""

    fibonacci(n)을 호출하면

    n >= 3
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    n = 2
    fibonacci(2) = fibonacci(1) + fibonacci(0)

    fibonacci(1) = 1
    fibonacci(0) = 0

"""


def fibonacci(n):
    cnt0 = [1, 0]
    cnt1 = [0, 1]
    for i in range(2, n + 1):
        cnt0.append((cnt0[i - 2] + cnt0[i - 1]))
        cnt1.append((cnt1[i - 2] + cnt1[i - 1]))

    return cnt0, cnt1


if __name__ == '__main__':

    T = int(input())
    for _ in range(T):
        N = int(input())

        cnt0, cnt1 = fibonacci(N)

        print(cnt0[N], cnt1[N])
