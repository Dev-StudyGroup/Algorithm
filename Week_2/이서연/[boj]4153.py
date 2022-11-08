'''
직각삼각형

- 문제 요약
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분.

- 입력 조건
입력은 여러 개의 테스트케이스로 주어지며, 마지막줄에는 0 0 0이 입력된다. 
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이.

- 출력 조건
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong" 출력
'''
import sys

while True:
    len = list(map(int, sys.stdin.readline().split()))
    if len == [0,0,0]:
        break
    len.sort()
    if len[0]**2 + len[1]**2 == len[2]**2:
        print('right')
    else:
        print('wrong')
