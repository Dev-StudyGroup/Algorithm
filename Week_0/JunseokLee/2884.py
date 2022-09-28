H,M=map(int,input().split())
M -= 45
if M<0:
    M=60+M
    H-=1
    if H<0:
        H=23
print(H, M)