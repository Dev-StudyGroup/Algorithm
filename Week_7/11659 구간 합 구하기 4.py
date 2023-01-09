import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    summary = [0]
    for i in range(len(numbers)):
        summary.append(numbers[i] + summary[i])
    for _ in range(M):
        start, end = map(int, input().split())
        print(summary[end] - summary[start - 1])
