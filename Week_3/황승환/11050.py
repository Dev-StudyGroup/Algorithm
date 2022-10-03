# 문제
# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))
#
# 출력
# \(\binom{N}{K}\)를 출력한다.
import math
n, k = map(int, input().split())
def by_math():
    return math.comb(n, k)
def by_brute_force():
    if k < 0 or k > n:
        return 0
    result = 1
    div = 1
    for i in range(k):
        result *= (n-i)
        div *= (k-i)
    return result//div
# print(by_math())
print(by_brute_force())
