import sys
input = sys.stdin.readline
for _ in range(int(input())):
    tmp = ""
    r, s = input().split()
    for i in s:
        print(i*int(r),end="")
    print()
