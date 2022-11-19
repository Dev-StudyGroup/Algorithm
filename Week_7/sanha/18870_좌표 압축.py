from collections import defaultdict

N = int(input())
numbers = list(map(int, input().split()))
tmp = numbers
tmp_set = list(set(tmp))
tmp_set.sort()
dic = defaultdict(int)

for i, e in enumerate(tmp_set):
    dic[e] = i

for number in numbers:
    print(dic[number], end=' ')
