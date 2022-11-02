import sys


input = sys.stdin.readline
t = int(input().rstrip())
def get_parent(x):
  if parent[x] != x:
    parent[x] = get_parent(parent[x])
  return parent[x]


def union_parent(a,b):
  a = get_parent(a)
  b = get_parent(b)

  if a != b:
    parent[b] = a
    friends[a] += friends[b]
  print(friends[a])

for _ in range(t):
  num = int(input())
  parent = {}
  friends = {}
  for i in range(num):
    a, b = input().split()
    if a not in parent:
      parent[a] = a
      friends[a] = 1
    if b not in parent:
      parent[b] = b
      friends[b] = 1
    union_parent(a, b)