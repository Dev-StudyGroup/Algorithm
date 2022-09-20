'''
A+B - 3

- 문제 요약
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

- 입력 조건
첫째 줄에 테스트 케이스의 개수 T가 주어짐.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어짐(0< A,B < 10)

- 출력 조건
각 테스트 케이스마다 A+B를 출력
'''
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)