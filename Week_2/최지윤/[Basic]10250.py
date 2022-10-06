def find(w, h, n):
    count = 0
    for i in range(1, w+1):
        for j in range(1, h+1):
            count += 1
            if count == n:
                return str(j) + str(i).zfill(2)

t = int(input())
result = []

for _ in range(t):
    h, w, n = map(int, input().split())
    room = find(w, h, n)
    result.append(room)

for r in result:
    print(r)