N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

def find_parent(a):
    if a != parents[a]:
        parents[a] = find_parent(parents[a])
    return parents[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        parents[b] = a

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

for i in range(1, N + 1):
    find_parent(i)

parent_set = set(parents)
print(len(parent_set) - 1)
