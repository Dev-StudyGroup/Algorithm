"""
최댓값
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
nums = []
for i in range(9):
    n = int(input())
    nums.append(n)

m = max(nums)
print(m)
print(nums.index(m) + 1)