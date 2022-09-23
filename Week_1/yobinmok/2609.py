def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(gcd(a,b))
print(a * b // gcd(a,b))

# 틀린 버전 -> 근데 왜 틀린지 모르겠음..
# a, b = map(int, input().split())
# for i in range(1, min(a,b)):
#     if a % i == 0 and b % i == 0:
#         factor = i
# multiple = a * b // factor
# print(factor)
# print(multiple)