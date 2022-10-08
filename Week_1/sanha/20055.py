from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
cnt = 0

while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    cnt += 1

    if sum(belt):
        for i in range(N - 2, -1, -1):
            if robot[i + 1] == 0 and robot[i] == 1 and belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0

    if belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(cnt)
