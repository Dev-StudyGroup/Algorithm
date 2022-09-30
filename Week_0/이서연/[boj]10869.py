'''
사칙연산

- 문제 요약
두 자연수 A와 B가 주어질 때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램

- 입력 조건
두 자연수 A,B가 주어짐(1 <= A,B <= 10000)

- 출력 조건
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B 출력
'''
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)