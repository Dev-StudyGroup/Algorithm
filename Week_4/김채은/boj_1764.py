from collections import defaultdict

n, m = map(int, input().split())

never_heard = defaultdict(int)
for _ in range(n):
    never_heard[input()] = 1

answer = []
for _ in range(m):
    person = input()
    if never_heard[person] > 0:
        answer.append(person)

answer.sort()

print(len(answer))
for a in answer:
    print(a)