"""
10814: 나이순 정렬
"""

n = int(input())

member = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    member.append([age, name])

member.sort(key = lambda x: x[0])

for i in member:
    print(i[0], end=" ")
    print(i[1])
