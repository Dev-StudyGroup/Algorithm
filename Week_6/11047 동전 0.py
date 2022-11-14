import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))

    result = 0
    while K != 0:
        for i in range(len(A) - 1, -1, -1):
            if K // A[i] > 0:
                result += K // A[i]
                K %= A[i]

    print(result)
