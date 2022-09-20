m,n = map(int,input().split())

for i in range(m,n+1):
    cnt = 0
    for x in range(1,i+1):
        if i%x == 0: cnt += 1
    if cnt <= 2:
        print(i)
