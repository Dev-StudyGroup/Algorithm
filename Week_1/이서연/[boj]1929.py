'''
소수 구하기

- 문제 요약
M 이상 N 이하의 소수를 모두 출력하는 프로그램

- 입력 조건
첫째 줄에 자연수 M과 N이 빈칸을 사이에 두고 주어짐(1 <= M <= N <= 1,000,000)
M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.

- 출력 조건
한 줄에 하나씩, 증가하는 순서대로 소수를 출력
'''
m, n = map(int, input().split())

for num in range(m, n+1):
    is_prime = True
    if num == 1:
        is_prime = False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:    # 1을 제외하고 약수가 있으면
            is_prime = False
            break
    if is_prime:
        print(num)
