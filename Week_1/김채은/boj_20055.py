# [BOJ] 20055 컨베이어 벨트 위의 로봇
# Time Taken: 1h

n, k = map(int, input().split())
strength = list(map(int, input().split()))
robot = [0 for _ in range(n)]

def rotate(strength, robot):
    strength = [strength[-1]] + strength[:2*n-1]
    robot = [0] + robot[:n-1]
    robot[n-1] = 0
    return strength, robot 

def move(strength, robot):
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and strength[i+1] >= 1:
            robot[i], robot[i+1] = 0, robot[i]
            strength[i+1] -= 1
    robot[n-1] = 0
    return strength, robot

def put_robot(strength, robot):
    if strength[0] > 0:
        robot[0] = 1
        strength[0] -= 1
    return robot

answer = 1
while True:
    strength, robot = rotate(strength, robot)

    strength, robot = move(strength, robot)

    robot = put_robot(strength, robot)

    if strength.count(0) >= k:
        break

    answer += 1

print(answer)
