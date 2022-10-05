K = int(input())
num = []
for _ in range(K):
    n = int(input())
    if n == 0 and len(num):
        num.pop()
    else:
        num.append(n)
print(sum(num))