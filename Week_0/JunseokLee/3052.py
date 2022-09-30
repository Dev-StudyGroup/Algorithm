num = set()
for _ in range(10):
    n = int(input())
    if n%42 not in num:
        num.add(n%42)
print(len(num))