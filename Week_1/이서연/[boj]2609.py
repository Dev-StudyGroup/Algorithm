'''
최대공약수와 최소공배수

- 문제 요약
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램

- 입력 조건
첫째 줄에 두 개의 자연수가 한칸 공백을 두고 주어짐.
10,000 이하의 자연수.

- 출력 조건
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 최소 공배수를 출력
'''
a, b = map(int, input().split())

for d in range(min(a,b), 0, -1):
    if a % d == 0 and b % d == 0:
        gcd = d
        break
lcm = int(a*b/gcd)
print(gcd)
print(lcm)
