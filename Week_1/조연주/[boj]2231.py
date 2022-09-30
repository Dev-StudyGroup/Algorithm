"""
분해합
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())

for i in range(n + 1):
    new = str(i)
    sum = 0
    for j in range(len(new)):
        sum += int(new[j])
    result = i + sum
    if result == n:
        print(i)
        break
    if i == n:
        print(0)
