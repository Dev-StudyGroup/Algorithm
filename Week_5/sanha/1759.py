from itertools import combinations

L, C = map(int, input().split())
numbs = list(map(str, input().split()))
combs = list(map(list, combinations(numbs, L)))
answer = []

def check(comb):
    consonants, vowels = 0, 0
    for c in comb:
        if c in ('a', 'e', 'i', 'o', 'u'):
            vowels += 1
        else:
            consonants += 1

    if vowels >= 1 and consonants >= 2:
        return True
    return False

for comb in combs:
    if check(comb):
        comb.sort()
        answer.append(''.join(comb))

answer.sort()
for a in answer:
    print(a)
