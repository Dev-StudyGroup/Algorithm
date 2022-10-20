n, k = map(int, input().split())

a, b, c = 1, 1, 1
for i in range(2, n+1):
    a *= i

for i in range(2, k+1):
    b *= i

for i in range(2, n-k+1):
    c *= i

print(a//(b*c))