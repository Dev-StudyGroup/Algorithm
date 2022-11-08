import math

#입력
n, m = map(int, input().split())
gcd_n=math.gcd(n,m)
print(gcd_n)
print(n*m//gcd_n)
