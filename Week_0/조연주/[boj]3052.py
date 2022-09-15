"""
나머지
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
count = [0] * 42
result = 0

for _ in range(10):
    n = int(input())
    count[n % 42] += 1

for i in range(42):
    if count[i] > 0:
        result += 1

print(result)
