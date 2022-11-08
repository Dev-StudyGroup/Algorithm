N = int(input())
people = []

for i in range(N):
    str = input().split()
    age, name = int(str[0]), str[1]
    people.append((age, i, name))

people.sort()
for person in people:
    print(person[0], end=' ')
    print(person[2])
