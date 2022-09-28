k = int(input())

result = []
for _ in range(k):
    n = int(input())
    if n == 0:
        result.pop()
    else:
        result.append(n)

print(sum(result))