# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
m, n = map(int, input().split())
primes = [True for _ in range(n+1)]
primes[1] = False
def get_primes(n):
    for i in range(2, n+1):
        for j in range(i+i, n+1, i):
            primes[j] = False
get_primes(n)
for i in range(m, n+1):
    if primes[i]:
        print(i)