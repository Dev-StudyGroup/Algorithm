import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline())) # int형으로 형변환!
nums.sort()
for num in nums:
    print(num)