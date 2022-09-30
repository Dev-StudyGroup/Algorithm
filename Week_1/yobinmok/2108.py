import sys
from collections import Counter

n = int(sys.stdin.readline())

nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
freq = Counter(nums).most_common()
most = 0; most_idx = []
# freq = [(숫자, 빈도수)]
if len(freq) > 1: # 입력값이 1개 이상일 때
    if freq[0][1] == freq[1][1]:
        mode = freq[1][0]
    else:
        mode = freq[0][0]
else:
    mode = freq[0][0]

print(round(sum(nums) / n)) # 1
print(nums[int(n / 2)]) # 2
print(mode) # 3
print(max(nums) - min(nums)) # 4