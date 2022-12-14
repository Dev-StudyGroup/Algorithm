'''
직사각형에서 탈출

- 문제 요약
직사각형 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0,0), 오른쪽 위 꼭짓점은 (w,h)에 있다.
(x,y) 위치에 있을 때 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램

- 입력 조건
첫째 줄에 x,y,w,h가 주어짐
1 <= w,h <= 1000
1 <= x <= w-1
1 <= y <= h-1
x,y,w,h는 정수

- 출력 조건
첫째 줄에 문제의 정답을 출력
'''
x,y,w,h = map(int, input().split())

result = min(x, w-x, y, h-y)
print(result)
