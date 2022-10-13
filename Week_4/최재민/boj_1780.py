from tabnanny import check


n = int(input())

paper = []

minus = 0
zero = 0
plus = 0

for _ in range(n):
  paper.append(list(map(int, input().split())))


def dfs(x, y, n):
  global minus,zero,plus

  check = paper[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if (paper[i][j] != check):
        for r in range(3):
          for c in range(3):
            dfs(x+r*n//3, y+c*n//3,n//3)
        return

  if check == -1:
    minus += 1
  elif check == 0:
    zero += 1
  else:
    plus += 1

dfs(0,0,n)
print(f'{minus}\n{zero}\n{plus}')