'''
A+B - 4

- 문제 요약
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

- 입력 조건
입력은 여러 개의 테스트 케이스로 이루어짐.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어짐(0< A,B < 10)

- 출력 조건
각 테스트 케이스마다 A+B를 출력
'''
# 테스트 케이스의 개수를 모르는 경우
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break