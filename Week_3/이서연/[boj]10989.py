'''
수 정렬하기 3

- 문제 요약
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램

- 입력 조건
첫째 줄에 수의 개수 N(1 <= N <= 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 수가 하나씩 주어진다. 
주어지는 수는 10,000 이하 자연수

- 출력 조건
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력.
'''
# 메모리 제한 8MB
import sys
n = int(sys.stdin.readline())
num = [0] * 10001
for _ in range(n):
    i = int(sys.stdin.readline())
    num[i] += 1

for j in range(len(num)):
    if num[j] != 0:
        for _ in range(num[j]):
            print(j)
