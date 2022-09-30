'''
'최대공약수와 최소공배수'
'''

a, b = map(int, input().split())

big = 1

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        big = i

small = big * (a // big) * (b//big)

print(big)
print(small)