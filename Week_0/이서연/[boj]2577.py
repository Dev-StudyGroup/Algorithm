'''
숫자의 개수

- 문제 요약
세 개의 자연수 A,B,C가 주어질때 A*B*C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇번씩 쓰였는지 구하는 프로그램

- 입력 조건
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어짐.
A,B,C는 모두 100보다 크거나 같고, 1000보다 작은 자연수

- 출력 조건
첫째 줄 A*B*C의 결과에 0이 몇번 쓰였는지 출력.
마찬가지로 둘째 줄부터 열번째 줄까지 결과에 1부터 9까지의 숫자가 각각 몇번 쓰였는지 한 줄에 하나씩 출력
'''
a = int(input())
b = int(input())
c = int(input())

result = a*b*c
count = [0] * 10
while result != 0:
    count[result % 10]+= 1
    result //= 10
for i in range(10):
    print(count[i])