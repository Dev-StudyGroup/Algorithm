N, M = map(int, input().split())
cards = list(map(int, input().split()))
Max = -1

def dfs(depth, cur, picked):
    global Max

    if depth == 3:
        total = sum(picked)
        if total <= M and total > Max:
            Max = total
        return

    for i in range(cur, N):
        picked.append(cards[i])
        dfs(depth + 1, i + 1, picked)
        picked.pop()

dfs(0, 0, [])
print(Max)
