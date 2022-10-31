import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    times = []
    for _ in range(N):
        times.append(list(map(int, input().split())))
    times.sort(key=lambda x: (x[1], x[0]))

    cnt = 1
    end_time = times[0][1]
    for i in range(1, N):
        if times[i][0] >= end_time:
            end_time = times[i][1]
            cnt += 1
    print(cnt)
