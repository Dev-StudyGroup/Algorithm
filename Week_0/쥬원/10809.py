import sys
input = sys.stdin.readline
s = input().rstrip()
for i in range(97, 123):
    try:
        print(s.index(chr(i)), end = ' ')
    except:
        print(-1, end = ' ')
