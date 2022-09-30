#입력
t = int(input())
for _ in range(t):
    n = input()
    count=0
    ans=0
    for i in n:
        if i=='O':
            count+=1
            ans+=count
        else:
            count=0
    print(ans)
