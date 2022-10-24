"""
1676: 팩토리얼 0의 개수
"""

n = int(input())
result = 1
count = 0

for i in str(factorial(n))[::-1]:
    if i == "0":
        count += 1
    else:
        break

print(count)

