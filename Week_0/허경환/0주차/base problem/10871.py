#입력
n, x = map(int, input().split())
ls=list(map(int, input().split()))
for i in ls:
    if i<x:
        print(i, end=' ')
        
