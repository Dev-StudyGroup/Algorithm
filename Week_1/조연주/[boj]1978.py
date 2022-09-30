"""
소수 찾기
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = 1000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

m = int(input())
nums = map(int, input().split())
cnt = 0

for num in nums:
    if a[num]:
        cnt += 1

print(cnt)
