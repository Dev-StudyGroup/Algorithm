'''
이항 계수 1

- 문제 요약
자연수 N과 정수 K가 주어졌을 때 이항계수를 구하는 프로그램.
( N
  k )

- 입력 조건
첫째 줄에 N과 K가 주어짐. (1 <= N <= 10, 0 <= K <= N)

- 출력 조건
( N
  k )를 출력
'''
# 이항 계수는 이항식을 이항 정리로 전개했을 때 각 항의 계수. 주어진 크기의 (순서 없는) 조합의 가짓수
# nCk
n, k = map(int, input().split())
result = 1
for i in range(1, k+1):
    result *= (n-i+1)
    result /= (i)
result = int(result)
print(result)
