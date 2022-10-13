from collections import defaultdict


n, m = map(int, input().split())

dbj = defaultdict(int)
for i in range(n+m):
  name = input()
  dbj[name] += 1

ans = []

for key in list(dbj.keys()):
  if dbj[key] == 2:
    ans.append(key)

print(len(ans))
for name in sorted(ans):
  print(name)