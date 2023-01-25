import sys
from collections import deque

input = sys.stdin.readline


def upper_to_lower(char):
    return chr(ord(char) + 32)


def find_start_point():
    global document
    start_points = []
    for i in range(h):
        if space[i][0] == ".":
            start_points.append([i, 0])
        elif space[i][0] == "$":
            start_points.append([i, 0])
            space[i][0] = "."
            document += 1
        elif 'a' <= space[i][0] <= 'z':
            keys.add(space[i][0])
            start_points.append([i, 0])
        elif 'A' <= space[i][0] <= 'Z':
            if upper_to_lower(space[i][0]) in keys:
                start_points.append([i, 0])
            else:
                doors.append((i, 0, space[i][0]))

        if space[i][w - 1] == ".":
            start_points.append([i, w - 1])
        elif space[i][w - 1] == "$":
            start_points.append([i, w - 1])
            space[i][w - 1] = "."
            document += 1
        elif 'a' <= space[i][w - 1] <= 'z':
            keys.add(space[i][w - 1])
            start_points.append([i, w - 1])
        elif 'A' <= space[i][w - 1] <= 'Z':
            if upper_to_lower(space[i][w - 1]) in keys:
                start_points.append([i, w - 1])
            else:
                doors.append((i, w - 1, space[i][w - 1]))

    for i in range(w):
        if space[0][i] == ".":
            start_points.append([0, i])
        elif space[0][i] == "$":
            start_points.append([0, i])
            space[0][i] = "."
            document += 1
        elif 'a' <= space[0][i] <= 'z':
            keys.add(space[0][i])
            start_points.append([0, i])
        elif 'A' <= space[0][i] <= 'Z':
            if upper_to_lower(space[0][i]) in keys:
                start_points.append([0, i])
            else:
                doors.append((0, i, space[0][i]))

        if space[h - 1][i] == ".":
            start_points.append([h - 1, i])
        elif space[h - 1][i] == "$":
            start_points.append([h - 1, i])
            space[h - 1][i] = "."
            document += 1
        elif 'a' <= space[h - 1][i] <= 'z':
            keys.add(space[h - 1][i])
            start_points.append([h - 1, i])
        elif 'A' <= space[h - 1][i] <= 'Z':
            if upper_to_lower(space[h - 1][i]) in keys:
                start_points.append([h - 1, i])
            else:
                doors.append((h - 1, i, space[h - 1][i]))
    return start_points


def bfs(points):
    global document
    new_keys = []
    for px, py in points:
        q = deque([[px, py]])
        visited[px][py] = 1
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if space[nx][ny] == '$':
                        document += 1
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                    if space[nx][ny] == '.':
                        visited[nx][ny] = 1
                        q.append([nx, ny])
                    elif 'A' <= space[nx][ny] <= 'Z':
                        if upper_to_lower(space[nx][ny]) in keys:
                            q.append([nx, ny])
                            visited[nx][ny] = 1
                        else:
                            doors.append((nx, ny, space[nx][ny]))
                    elif 'a' <= space[nx][ny] <= 'z':
                        keys.add(space[nx][ny])
                        new_keys.append(space[nx][ny])
                        q.append([nx, ny])
                        visited[nx][ny] = 1
    return new_keys


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    test_case = int(input())
    for t in range(test_case):
        h, w = map(int, input().split())
        keys = set()
        doors = []
        document = 0
        space = []
        visited = [[0 for _ in range(w)] for _ in range(h)]
        for _ in range(h):
            space.append(list(" ".join(input().rstrip()).split()))

        key_list = list(" ".join(input().rstrip()).split())
        if key_list[0] != "0":
            for k in range(len(key_list)):
                keys.add(key_list[k])

        start_points = find_start_point()
        bfs(start_points)

        while True:
            new_keys = set()
            for door in doors:
                x, y, char = door
                if not visited[x][y] and upper_to_lower(char) in keys:
                    new_keys.add(tuple(bfs([[x, y]])))
            if len(new_keys) == 0:
                break

        print(document)
