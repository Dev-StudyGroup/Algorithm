C = int(input())

def dfs(total, depth):
    global answer

    if depth == 11:
        answer = max(answer, total)
        return

    for i in range(11):
        if not visited[i] and G[depth][i]:
            visited[i] = True
            dfs(total + G[depth][i], depth + 1)
            visited[i] = False

for _ in range(C):
    G = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    visited = [False] * 11
    dfs(0, 0)
    print(answer)
