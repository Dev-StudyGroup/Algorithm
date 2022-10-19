"""
덩치
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())
people = []

for i in range(n):
    h, w = map(int, input().split())
    people.append((h, w))

rank = []

for i in range(n):
    k = 1
    for j in range(n):
        if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
            k += 1
    rank.append(k)

print(*rank)