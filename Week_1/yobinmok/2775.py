t = int(input())

for i in range(t):
    k = int(input()) # k층
    n = int(input()) # n호
    floor0 = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            floor0[j] += floor0[j-1]
    print(floor0[-1])
