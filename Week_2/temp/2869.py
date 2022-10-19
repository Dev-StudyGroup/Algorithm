"""
2869: 달팽이는 올라가고 싶다
"""
import sys

a, b, v = map(int, sys.stdin.readline().split())
# a: 낮에 올라가는 높이, b: 밤에 미끄러지는 높이, v:나무의 높이

day = int((v - b) / (a - b)) # 낮에 나무를 다 올랐을 때
if (v - b) % (a - b) != 0: 
    day += 1
print(day)
