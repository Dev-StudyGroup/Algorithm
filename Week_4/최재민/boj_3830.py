#풀이 시작: 15시 39분
#풀이 종료: 16시 59분
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_parent(x):
  if x == parent[x]:
    return x
  else:
    r = get_parent(parent[x])
    weight[x] += weight[parent[x]]
    parent[x] = r 
    return parent[x]


def union_parent(a,b, w):
  aParent = get_parent(a)
  bParent = get_parent(b)

  if aParent != bParent:
    weight[bParent] = weight[a] - weight[b] + w
    parent[bParent] = aParent


while True:
  n, m = map(int,input().rstrip().split())
  if n == 0 and m == 0 : 
    break
  parent = [i for i in range(n+1)]
  weight = [0 for i in range(n+1)]
  for i in range(m):
    work = list(input().rstrip().split())
    a, b= int(work[1]), int(work[2])
    if work[0] == '!':
      union_parent(a, b, int(work[3]))
    else:
      if (get_parent(a) != get_parent(b)):
        print("UNKNOWN")
      else:
        print(weight[b] - weight[a])