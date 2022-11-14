"""

    케빈 베이컨 6단계 법칙

    이어진 단계가 가장 작은 사람을 케빈 베이컨이라고 한다.

    유저 5명
    1 : 3
    1 : 4
    4 : 2
    3 : 3
    4 : 5


"""
from collections import deque


def bfs(start, user_cnt, g, reach_count):
    queue = deque()
    visited = [0] * (user_cnt + 1)
    reach_count = [1000001] * (user_cnt + 1)
    count = 0
    queue.append([start, count])
    while queue:
        current, count = queue.popleft()
        if not visited[current]:
            visited[current] = 1
            reach_count[current] = min(reach_count[current], count)
            count += 1
            for next_user in g[current]:
                if not visited[next_user]:
                    queue.append([next_user, count])
    reach_count = [0 if count == 1000001 else count for count in reach_count]
    return sum(reach_count)


if __name__ == '__main__':
    from collections import defaultdict

    N, M = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    kevin_bacon = []
    for i in range(1, N + 1):
        kevin_bacon.append([i, bfs(i, N, graph, [])])

    kevin_bacon.sort(key=lambda x: [x[1], x[0]])
    print(kevin_bacon[0][0])
