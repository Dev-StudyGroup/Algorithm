import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    num = [0] * 12
    num[1] = 1
    num[2] = 2
    num[3] = 4
    for i in range(4, 12):
        num[i] = num[i - 1] + num[i - 2] + num[i - 3]

    for _ in range(T):
        n = int(input())
        print(num[n])
