from collections import Counter

tc = int(input())
for _ in range(tc):
    n = int(input())
    clothes = []
    answer = 1
    for _ in range(n):
        k, item = input().split()
        clothes.append(item)

    clothes_cnt = Counter(clothes)
    for cnt in clothes_cnt.values():
        answer *= cnt + 1

    print(answer - 1)
