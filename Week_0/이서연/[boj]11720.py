'''
숫자의 합

- 문제 요약
N개의 숫자가 공백없이 주어질때 이를 모두 합해서 출력하는 프로그램

- 입력 조건
첫째 줄에 숫자의 개수 N(1 <= N <= 100)이 주어짐.
둘째 줄에 숫자 N개가 공백없이 주어짐

- 출력 조건
입력으로 주어진 숫자 N개의 합을 출력
'''
n = int(input())
num = input()
result = 0
for i in range(n):
    result = result + int(num[i])
print(result)