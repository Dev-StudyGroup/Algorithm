N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()
for point in points:
    print(point[0], point[1])
