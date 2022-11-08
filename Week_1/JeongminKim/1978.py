"""

    문제 :
    주어진 수 N개 중에서 소수가 몇 개인지 출력

"""

N = int(input())
num = list(map(int, input().split()))

def is_prime_number(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cnt = 0
for n in num:
    if is_prime_number(n):
        cnt += 1

print(cnt)