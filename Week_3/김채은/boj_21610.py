# [BOJ] 21610 마법사 상어와 비바라기
# Time Taken: 50m

from collections import defaultdict

def move(y, x, d, s):
    dy, dx = direction[d]
    
    def isNegative(point):
        if point < 0:
            return point + n
        else:
            return point

    ny, nx = (y + dy * s) % n, (x + dx * s) % n    
    ny, nx = isNegative(ny), isNegative(nx)

    return ny, nx

def rain():
    for cloud in cloud_list:
        y, x = cloud
        buckets[y][x] += 1

def water_copy():
    diagonal_index = [2, 4, 6, 8]

    def in_range(i, j):
        if 0 <= i < n and 0 <= j < n:
            return True
        else:
            return False

    for cloud in cloud_list:
        y, x = cloud
        water_bucket_count = 0

        for di in diagonal_index:
            dy, dx = direction[di]
            ny, nx = y + dy, x + dx
            
            if in_range(ny, nx) and buckets[ny][nx]:
                water_bucket_count += 1
            
        buckets[y][x] += water_bucket_count

def make_cloud():
    new_cloud = defaultdict(int)

    for i in range(n):
        for j in range(n):
            if buckets[i][j] >= 2 and not cloud_dict[(i, j)]:
                new_cloud[(i, j)] = 1
                buckets[i][j] -= 2

    return new_cloud

def water_count():
    count = 0

    for bucket in buckets:
        count += sum(bucket)

    return count

if __name__ == "__main__":

    n, m = map(int, input().split())
    buckets = [list(map(int, input().split())) for _ in range(n)]
    move_list = [list(map(int, input().split())) for _ in range(m)]

    direction = {
        1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
        5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)
    }

    cloud_dict = defaultdict(int)

    initial_cloud = [(n-2, 0), (n-1, 0), (n-2, 1), (n-1, 1)]

    for ic in initial_cloud:
        cloud_dict[ic] = 1

    cloud_list = cloud_dict.keys()

    for mv in move_list:
        d, s = mv

        new_cloud = defaultdict(int)

        for cloud in cloud_list:
            y, x = cloud
            new_cloud[move(y, x, d, s)] = 1

        cloud_dict = new_cloud
        cloud_list = cloud_dict.keys()

        rain()
        water_copy()

        cloud_dict = make_cloud()
        cloud_list = cloud_dict.keys()

    print(water_count())
