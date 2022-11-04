import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    S = input()
    count = 0
    result = 0
    i = 0
    while i < M:
        if S[i:i + 3] == 'IOI':
            i += 2
            count += 1
            if count == N:
                result += 1
                count -= 1
        else:
            i += 1
            count = 0

    print(result)
