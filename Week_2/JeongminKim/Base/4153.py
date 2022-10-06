"""

    주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시요

    a*2 + b*2 - c*2 = 0

"""
import sys

while 1:
    sides = list(map(int, sys.stdin.readline().split()))

    if sum(sides) == 0:
        break
    sides.sort(reverse=False)
    a = sides[0]
    b = sides[1]
    c = sides[-1]

    if (a ** 2 + b ** 2 - c ** 2) == 0:
        print('right')
    else:
        print('wrong')
