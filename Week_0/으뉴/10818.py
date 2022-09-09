import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
print(f'{min(arr)} {max(arr)}')
