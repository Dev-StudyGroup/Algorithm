"""
컨베이어 벨트 위의 로봇
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import deque

n, k = map(int, input().split())
array = list(map(int, input().split()))
robot_list = [0] * (2 * n)
robot = deque(robot_list)
queue = deque(array)
count = 0

while 1:
    count += 1

    # 1
    queue.appendleft(queue.pop())
    if robot[n - 1] == 1:
        robot[n - 1] = 0
    robot.appendleft(robot.pop())

    # 2
    for i in range(2 * n - 1, -1, -1):
        if i == (2 * n - 1):
            if robot[i] > 0 and robot[0] == 0 and queue[0] > 0:
                robot[2 * n - 1] = 0
                robot[0] = 1
                queue[0] -= 1
        elif i == n - 1:
            if robot[n - 1] == 1:
                robot[n - 1] = 0
        else:
            if robot[i] > 0 and robot[i + 1] == 0 and queue[i + 1] > 0:
                robot[i] = 0
                robot[i + 1] = 1
                queue[i + 1] -= 1

    # 3
    if queue[0] > 0 and robot[0] == 0:
        robot[0] = 1
        queue[0] -= 1

    # 4
    if queue.count(0) >= k:
        break

print(count)
