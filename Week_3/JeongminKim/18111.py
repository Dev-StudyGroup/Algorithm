"""

    세로 N 가로 M 크기의 집터

    집터 맨 왼쪽 위의 좌표는 0, 0

    집터의 땅의 높이를 일정하게 바꾸는 것

    1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. => 2초
    2. 인벤토리에서 블록 하나를 꺼내어 좌표(i, j)의 가장 위에 있는 블록 위에 놓는다. => 1초

    최소 시간과 해당 작업 후의 땅의 높이 출력

"""
import sys
from collections import Counter


def cal_time(aim_h):
    global land
    time = 0
    use_blocks = 0
    get_blocks = 0
    for h, c in land.items():
        # aim_h 보다 높은 h지형은 땅을 파서 인벤토리에 넣고, 시간은 2초 걸린다.
        if h > aim_h:
            get_blocks += c * (h - aim_h)
            time += 2 * c * (h - aim_h)
        # 반대로 h 지형은 블럭을 쌓아서 사용하고 시간은 1초 걸린다.
        elif h < aim_h:
            use_blocks += c * (aim_h - h)
            time += 1 * c * (aim_h - h)

    return use_blocks, get_blocks, time, aim_h


if __name__ == '__main__':

    N, M, B = map(int, sys.stdin.readline().split())

    times = []
    land = Counter()
    blocks_ground = 0
    for _ in range(N):
        m_i_ground = list(map(int, sys.stdin.readline().split()))
        blocks_ground += sum(m_i_ground)
        land += Counter(m_i_ground)

    max_limit_height = 256
    best_h = 0
    max_limit_time = 256 * 500 * 500
    best_time = max_limit_time
    max_h = max(land)
    min_h = min(land)

    for h in range(min_h, max_h + 1):
        used_block, get_block, time, aim_h = cal_time(h)
        if blocks_ground + B >= h * N * M:
            if max_limit_time > time:
                if time <= best_time:
                    best_h = aim_h
                    best_time = time

print(f'{best_time} {best_h}')
