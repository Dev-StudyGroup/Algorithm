import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

maximumm = max(arr)
print(sum([i / maximumm * 100 for i in arr]) / n)
