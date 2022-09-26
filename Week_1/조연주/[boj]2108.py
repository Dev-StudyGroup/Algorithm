"""
통계학
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import Counter
import sys

n = int(input())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline())) # input 쓰면 시간초과...
    
nums.sort()
most = Counter(nums).most_common(2)

print(round(sum(nums)/n))
print(nums[n//2])
if n > 1:
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
else:
    print(most[0][0])
print(nums[-1] - nums[0])
