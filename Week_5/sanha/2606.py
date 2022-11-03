N = int(input())
pairs = int(input())
parents = [i for i in range(N + 1)]
cnt = 0

def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(pairs):
    a, b = map(int, input().split())
    union(a, b)

num = parents[1]
for i in range(2, N + 1):
    if find_parent(i) == num:
        cnt += 1
print(cnt)
