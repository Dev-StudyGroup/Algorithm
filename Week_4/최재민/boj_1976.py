n = int(input())
m = int(input())

def get_parent(x):
  if parent[x] != x:
    parent[x] = get_parent(parent[x])
  return parent[x]


def union_parent(a,b):
  a = get_parent(a)
  b = get_parent(b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b


parent = [i for i in range(n)]
for i in range(n):
  link = list(map(int,input().split()))
  for j in range(n):
    if link[j] == 1:
      union_parent(i,j)

parent = [-1] + parent
path = list(map(int,input().split()))
start = parent[path[0]]
for i in range(1,m):
  if parent[path[i]] != start:
    print("NO")
    break
else:
  print("YES")