'''
소수 찾기

- 문제 요약
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램

- 입력 조건
첫 줄에 100 이하의 수 N이 주어짐.
다음으로 N개의 수가 빈칸을 두고 주어짐(1000 이하의 자연수)

- 출력 조건
주어진 수들 중 소수의 개수 출력
'''
def is_prime(num):
    is_prime = True
    if num == 1:
        is_prime = False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:    # 1을 제외하고 약수가 있으면
            is_prime = False
            break
    return is_prime

n = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if is_prime(num):
        count += 1
print(count)
