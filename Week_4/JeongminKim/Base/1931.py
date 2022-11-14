"""

    한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.

    각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 갯수를 찾아보자

    회의는 한번 시작하면 중간에 중단 될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

    회의의 시작시간과 끝나는 시간이 같을 수도 있다.

"""
import sys

if __name__ == '__main__':
    N = int(input())
    time_list = []

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        time_list.append([start, end])

    time = sorted(time_list, key=lambda a: a[0])
    time = sorted(time, key=lambda a: a[1])
    last = 0
    count = 0

    for i, j in time:
        if i >= last:
            count += 1
            last = j

    print(count)
