t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    
    count = 0
    for i in range(1, w+1):
        for j in range(1, h+1):
            count += 1
            if count == n:
                print(j * 100 + i)
                break
            