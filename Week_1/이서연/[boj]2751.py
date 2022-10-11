'''
수 정렬하기 2

- 문제 요약
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램

- 입력 조건
첫째 줄에 수의 개수 N(1 <= N <= 1,000,000)이 주어짐.
둘째 줄부터 N개의 줄에 수가 주어짐. (절댓값이 1,000,000보다 작거나 같은 정수)
수는 중복되지 않음

- 출력 조건
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
'''
import sys
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

for x in num:
    print(x)
