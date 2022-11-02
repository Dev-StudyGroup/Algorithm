'''
'수 정렬하기 3'
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
array = defaultdict(int)

for i in range(N):
    num = int(input())
    array[num] += 1

array = dict(sorted(array.items(), key=lambda x:x[0]))

for i in array:
    for j in range(array[i]):
        print(i)
