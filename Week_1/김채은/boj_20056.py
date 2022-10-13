# [BOJ] 20056 마법사 상어와 파이어볼
# Time Taken: 1h 24m

from collections import defaultdict

n, m, k = map(int, input().split())
fireball = defaultdict(list)

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball[(r, c)].append((m, s, d))

direction = {
    0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1),
    4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)
}

def move():
    new_fireball = defaultdict(list)

    for location, balls in fireball.items():
        for ball in balls:
            r, c = location
            m, s, d = ball

            nr, nc = (r + direction[d][0] * s) % n, (c + direction[d][1] * s) % n

            if nr <= 0:
               nr += n
            if nc <= 0:
               nc += n

            new_fireball[(nr, nc)].append(ball)

    return new_fireball

def after_move():
    new_fireball = fireball.copy()
    for location, balls in fireball.items():

        if len(balls) >= 2:

            new_balls = []
            m_sum, s_sum = 0, 0
            d_first, d_all_flag = balls[0][2] % 2, True

            for ball in balls:
                m, s, d = ball
                m_sum += m
                s_sum += s
                if d_first != d % 2:
                    d_all_flag = False

            r, c = location
            if m_sum // 5 == 0:
                new_fireball[(r, c)] = []
            else:
                start = 0 if d_all_flag else 1

                for i in range(4):
                    new_balls.append((m_sum//5, s_sum//len(balls), start + 2 * i))

                new_fireball[(r, c)] = new_balls
                
    return new_fireball

for _ in range(k):
    fireball = move()
    fireball = after_move()

answer = 0

for location, balls in fireball.items():
    for ball in balls:
        answer += ball[0]

print(answer)
