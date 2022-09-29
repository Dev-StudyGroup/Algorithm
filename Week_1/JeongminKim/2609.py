"""

    두 개의 자연수를 입력받아

    최대 공약수(gcd)와 최소 공배수(lcm)를 출력

"""
import math

A, B = map(int, input().split())

print(math.gcd(A, B))
print(math.lcm(A, B))
