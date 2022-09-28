# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
n = int(input())
nums = list(map(int, input().split()))
rn = max(nums)
primes = [True for _ in range(rn+1)]
def get_prime():
    primes[1] = False
    for i in range(2, rn+1):
        for j in range(i+i, rn+1, i):
            primes[j] = False
get_prime()
answer = 0
for num in nums:
    if primes[num]:
        answer += 1
print(answer)