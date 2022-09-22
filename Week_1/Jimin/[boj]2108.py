'''
'통계학'
'''
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array.sort()
print(round(sum(array)/N))
print(array[N//2])

most = Counter(array).most_common()
print(most)
if len(most) > 1:
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
else:
    print(most[0][0])


print(array[N-1]-array[0])