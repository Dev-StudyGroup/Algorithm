'''
마인크래프트

- 문제 요약
세로 N, 가로 M 크기의 집터 내의 땅의 높이를 일정하게 바꾸어야 함. 집터 맨 왼쪽 위의 좌표는 (0,0)
다음과 같은 두 종류의 작업을 할 수 있다.
    1. 좌표 (i,j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. - 2초 걸림
    2. 인벤토리에서 블록하나를 꺼내어 좌표 (i,j)의 가장 위에 있는 블록 위에 놓는다. - 1초 걸림
땅 고르기 작업에 걸리는 최소 시간과 땅의 높이 출력.
단, 집터 바깥에서 블록을 가져올 수 없으며, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어있다.
땅의 높이는 256블록을 초과할 수 없고, 음수가 될 수 없다.

- 입력 조건
첫째 줄에 N, M, B가 주어진다.
1 <= M,N <= 500
0 <= B <= 6.4 * 10**7
둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다.
(i+2)번째 줄의 (j+1)번째 수는 좌표 (i,j)에서의 땅의 높이를 나타낸다.
땅의 높이는 256보다 작거나 같은 자연수 또는 0.

- 출력 조건
첫째 줄에 땅을 고르는데 걸리는 시간과 땅의 높이를 출력.
답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력.
'''
import sys

n, m, b = map(int, sys.stdin.readline().split())
ground_dict = {}
for _ in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        if i in ground_dict:
            ground_dict[i] += 1
        else:
            ground_dict[i] = 1

case = []

for cur_height in range(0,257):
    del_count = 0
    add_count = 0

    for key in ground_dict:
        if key > cur_height:
            del_count += (key - cur_height) * ground_dict[key]
        else:
            add_count += (cur_height - key) * ground_dict[key]

    if add_count <= del_count + b:
        time = del_count *2 + add_count
        case.append([time, cur_height])

result = min(case, key=lambda x:(x[0], -x[1]))
print(result[0], result[1])
