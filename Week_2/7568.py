"""
7568: 덩치
"""

# 키, 몸무게 = (x, y)
# 키와 몸무게가 모두 커야 자신보다 덩치가 큰 것
# 자신보다 더 큰 덩치의 사람이 k명이면 자신의 등수는 k+1등

n = int(input())
person = []; 
rank = [1 for _ in range(n)]
for i in range(n):
    person.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i != j:
            if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
                rank[i] += 1

for i in rank:
    print(i, end=" ")
    