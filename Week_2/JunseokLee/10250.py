import math

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    w = math.ceil(N / H)
    h = N % H
    if h == 0:
        h = H
    print(h * 100 + w)
