"""
2839: 설탕배달
"""

n = int(input())
sugar = []
if n % 5 == 0:
    sugar.append(n//5)
elif n % 3 == 0:
    sugar.append(n//3)

for i in range(1, n//5 + 1):
    if (n - (5 * i)) % 3 == 0:
        sugar.append(i + (n - (5 * i))//3)

if len(sugar) != 0:
    print(min(sugar))
else:
    print("-1")
    