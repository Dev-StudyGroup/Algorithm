'''
기찍 N

- 문제 요약
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램

- 입력 조건
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어짐

- 출력 조건
첫째 줄부터 N번째 줄까지 차례대로 출력
'''
n = int(input())
for i in range(n):
    print(n-i)

# 반복문 반대로
# for i in range(n, 0, -1):
#     print(i)

# for i in reversed(range(1, n+1)):
#     print(i)