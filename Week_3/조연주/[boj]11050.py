"""
이항 계수 1
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
def multiplication(a, b):
    mul = 1
    for x in range(b, a + 1):
        mul *= x
    return mul

n, k = map(int, input().split())
if k == 0:
    print(1)
elif k == 1:
    print(n)
else:
    numerator = multiplication(n, n - k + 1)
    denominator = multiplication(k, 1)
    print(numerator//denominator)
