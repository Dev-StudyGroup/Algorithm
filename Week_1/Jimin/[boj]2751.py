'''
'수 정렬하기 2'
'''
import sys
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)