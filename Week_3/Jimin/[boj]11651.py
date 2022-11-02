'''
'좌표 정렬하기 2'
'''
import sys
input = sys.stdin.readline

array = []
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    array.append([b, a])

array.sort()

for i in array:
    print(i[1], i[0])
