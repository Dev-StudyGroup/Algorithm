"""
최대공약수와 최소공배수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
