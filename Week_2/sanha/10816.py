from collections import defaultdict

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
choices = list(map(int, input().split()))
dic = defaultdict(int)

for card in cards:
    dic[card] += 1

for choice in choices:
    print(dic[choice], end=' ')
