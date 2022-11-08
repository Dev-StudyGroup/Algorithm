'''
'좌표 정렬하기'
'''
import sys
input = sys.stdin.readline

array = []
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    array.append([a, b])

array.sort()

for i in array:
    print(i[0], i[1])
