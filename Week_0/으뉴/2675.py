import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, string = input().split()

    for s in string:
        print(s*int(n), end='')
    print()
