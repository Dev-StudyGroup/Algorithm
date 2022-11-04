import heapq
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        k = int(input())
        max_q = []
        min_q = []
        count = 0
        visited = [0] * (k + 1)

        for i in range(1, k + 1):
            command, num = input().split()

            if command == 'I':
                count += 1
                heapq.heappush(max_q, (-int(num), i))
                heapq.heappush(min_q, (int(num), i))

            elif command == 'D':
                if count:
                    count -= 1
                    if num == '1':
                        while max_q and visited[max_q[0][1]]:
                            n, index = heapq.heappop(max_q)
                        if max_q:
                            visited[heapq.heappop(max_q)[1]] = 1
                    elif num == '-1':
                        while min_q and visited[min_q[0][1]]:
                            n, index = heapq.heappop(min_q)
                        if min_q:
                            visited[heapq.heappop(min_q)[1]] = 1

        while max_q and visited[max_q[0][1]]:
            n, index = heapq.heappop(max_q)

        while min_q and visited[min_q[0][1]]:
            n, index = heapq.heappop(min_q)

        if count:
            print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
            continue
        print("EMPTY")
