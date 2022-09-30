num = set()
for i in range(10):
    n = int(input())
    num.add(n % 42)

print(len(num))