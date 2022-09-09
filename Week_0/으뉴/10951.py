import sys

input = sys.stdin.readline
while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)
