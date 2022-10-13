from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

poketmonName = {}
poketmonNum = {}
for i in range(n):
  name = input().rstrip()
  poketmonName[i] = name
  poketmonNum[name] = i 

for _ in range(m):
  quiz = input().rstrip()
  if quiz.isdigit() == True:
    print(poketmonName[int(quiz)-1])
  else:
    print(poketmonNum[quiz]+1)
