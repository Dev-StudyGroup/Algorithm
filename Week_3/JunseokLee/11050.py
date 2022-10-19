N,K=map(int,input().split())
a, b = 1, 1
n = K
for i in range(n):
    a *= N
    b *= K
    N -= 1
    K -= 1
print(a//b)