"""

    최소 힙이 있다.

    최소 힙을 이용하여 다음과 같은 연산을 지원

    1. 배열에 자연수 x를 넣는다.
    2. 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

    sys.stdin.readline 사용할 것
"""
import heapq
import sys


def is_empty(ls):
    return len(ls) == 0


def heap_func(ls, num):
    if num == 0:
        if is_empty(ls):
            print(0)
        else:
            print(heapq.heappop(ls))
        # try:
        #     print(heapq.heappop(ls))
        # except IndexError:
        #     print(0)
        return

    heapq.heappush(ls, num)


if __name__ == '__main__':
    h = []
    N = int(input())

    for _ in range(N):
        x = int(sys.stdin.readline())
        heap_func(h, x)
