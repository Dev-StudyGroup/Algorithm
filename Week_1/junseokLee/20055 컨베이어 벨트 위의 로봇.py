from collections import deque

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = [0] * N


def belt_move():
    global robot
    A.rotate()
    robot = [0] + robot[:N - 1]
    robot[N - 1] = 0


def robot_move():
    for i in range(N - 1, 0, -1):
        if A[i] and not robot[i] and robot[i - 1]:
            robot[i - 1] = 0
            robot[i] = 1
            A[i] -= 1
    robot[N - 1] = 0


def push_robot():
    if A[0]:
        robot[0] = 1
        A[0] -= 1


def solution():
    count = 0
    while True:
        count += 1
        belt_move()
        robot_move()
        push_robot()
        if A.count(0) >= K:
            break
    print(count)


solution()
