def spin(query, G):
    sx, sy, ex, ey = query
    tmp = G[sx][sy]
    Min = tmp
    for i in range(sx, ex):
        G[i][sy] = G[i + 1][sy]
        Min = min(Min, G[i][sy])

    for i in range(sy, ey):
        G[ex][i] = G[ex][i + 1]
        Min = min(Min, G[ex][i])

    for i in range(ex, sx, -1):
        G[i][ey] = G[i - 1][ey]
        Min = min(Min, G[i][ey])

    for i in range(ey, sy, -1):
        G[sx][i] = G[sx][i - 1]
        Min = min(Min, G[sx][i])
    G[sx][sy + 1] = tmp
    return Min


def solution(rows, columns, queries):
    answer = []
    G = [[0] * (columns + 1) for _ in range(rows + 1)]
    cnt = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            G[i][j] = cnt
            cnt += 1

    for query in queries:
        answer.append(spin(query, G))

    return answer
