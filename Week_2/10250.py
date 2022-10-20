#입력
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    
    #yy와 xx
    if n<h:
        yy=str(n)
        xx='01'
    else:
        if n%h==0:
            yy=str(h)
        else:
            yy=str(n%h)
        
        if n%h==0:
            if n//h>=10:
                xx=str(n//h)
            else:
                xx='0'+str(n//h)
        else:
            if n//h+1>=10:
                xx=str(n//h+1)
            else:
                xx='0'+str(n//h+1)
    #출력
    print(int(yy+xx))
