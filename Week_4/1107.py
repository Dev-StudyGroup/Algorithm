"""
1107: 리모컨
* 브루트 포스로 가능한 채널의 모든 경우의 수를 다 계산해 최소값을 구한다. 
"""
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

min_count = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums)-1:
            min_count = min(min_count, abs(int(nums)-n) + len(nums))

print(min_count)
