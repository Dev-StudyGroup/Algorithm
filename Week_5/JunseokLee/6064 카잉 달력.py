import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().split())
        end = M*N
        while x <= end:
            if (x - y) % N == 0:
                break
            x += M
        if x > end:
            print(-1)
            continue
        print(x)
