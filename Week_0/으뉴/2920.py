import sys

input = sys.stdin.readline
arr = list(map(int,input().split()))

if list(range(1,9)) == arr: print("ascending")
elif list(range(8, 0, -1)) == arr: print("descending")
else: print("mixed")
