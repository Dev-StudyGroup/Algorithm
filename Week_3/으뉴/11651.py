import sys
input = sys.stdin.readline
arr = [input() for _ in range(int(input()))]
arr = sorted(arr, key = lambda x: (int(x.split()[1]), int(x.split()[0])))
print(''.join(arr))
