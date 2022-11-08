from collections import defaultdict
num = defaultdict(int)
N = int(input())
cards = list(map(int, input().split()))
for n in cards:
    num[n] += 1
M = int(input())
arr = list(map(int, input().split()))
for n in arr:
    print(num[n], end=' ')