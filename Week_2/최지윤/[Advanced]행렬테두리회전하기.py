def solution(rows, columns, queries):
    answer = []
    data = [[0] * columns for _ in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(columns):
            count += 1
            data[i][j] = count

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    for x1, y1, x2, y2 in queries:
        data_cp = [d[:] for d in data]
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        x, y, nx, ny, d = x1, y1, -1, -1, 0
        min_val = 1e9

        while (nx, ny) != (x1, y1):
            nx, ny = x + dx[d], y + dy[d]
            
            if nx < x1 or nx > x2 or ny < y1 or ny > y2:
                d = (d + 1) % 4
                nx, ny = x + dx[d], y + dy[d]
                
            data_cp[nx][ny] = data[x][y]
            min_val = min(min_val, data_cp[nx][ny])
            x, y = nx, ny
            
        data = data_cp
        answer.append(min_val)
            
    return answer