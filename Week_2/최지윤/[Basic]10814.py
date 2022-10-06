n = int(input())

member = []
for _ in range(n):
    member.append(tuple(map(str, input().split())))

member.sort(key = lambda x : int(x[0]))
for age, name in member:
    print(age, name)