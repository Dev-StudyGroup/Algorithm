N, K = map(int, input().split())
tools = list(map(int, input().split()))
cnt = 0
consents = []

for i in range(K):
    if tools[i] in consents:
        continue

    if len(consents) < N:
        consents.append(tools[i])
        continue

    idxs = []
    plugged = True
    for j in range(N):
        if consents[j] in tools[i:]:
            idx = tools[i:].index(consents[j])
        else:
            idx = 101
            plugged = False

        idxs.append(idx)

        if not plugged:
            break

    out = idxs.index(max(idxs))
    del consents[out]
    consents.append(tools[i])
    cnt += 1

print(cnt)
