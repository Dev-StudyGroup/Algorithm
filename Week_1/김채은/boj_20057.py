# [BOJ] 20057 마법사 상어와 토네이도
# Time Taken: 1h 53m

import math

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

global answer
answer = 0

def tonado():
    global answer

    y, x = n//2, n//2
    cur_dir = 0
    
    count = 1

    while True:
        for _ in range(2):
            for _ in range(count):
                y, x = y + direction[cur_dir][0], x + direction[cur_dir][1]
                
                answer += spread(y, x, cur_dir)
                
                if (y, x) == (0, 0):
                    return answer
            
            cur_dir = (cur_dir + 1) % 4
        
        count += 1

def in_range(y, x):
    if 0<=y<n and 0<=x<n:
        return True
    return False

def spread(y, x, cur_dir):
    sand = board[y][x]
    out = 0

    spread = {
        10: [(-1, -1), (1, -1), (1, 1), (-1, 1)],
        1: [(1, 1), (-1, 1), (-1, -1), (1, -1)],

        7: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        2: [(-2, 0), (2, 0), (0, -2), (0, 2)],

        5: [(0, -2), (2, 0), (0, 2), (-2, 0)],
        'a': [(0, -1), (1, 0), (0, 1), (-1, 0)]
    }


    for pc, loc in spread.items():
        locs = []
        if pc in [10, 1]:
            locs = [loc[cur_dir], loc[(cur_dir+1)%4]]

        elif pc in [7, 2]:
            if cur_dir % 2 == 0:
                locs = [loc[0], loc[1]]

            else:
                locs = [loc[2], loc[3]]
        else:
            locs = [loc[cur_dir]]

        for i, j in locs:
            if pc != 'a':
                sp = math.floor(board[y][x] * pc / 100)
            else:
                sp = sand

            if in_range(y+i, x+j):
                board[y+i][x+j] += sp
            else:
                out += sp
            sand -= sp

    board[y][x] = 0

    return out 

print(tonado())
