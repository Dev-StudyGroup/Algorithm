#입력
n = int(input())

#문제유형파악
#브루트포스로 666부터 1씩 상승시키면서 각 수에 666이 들어가는지 파악

check=666
while(n):
    if "666" in str(check):
        n-=1
    check+=1
    
    
    
    
#출력
print(check-1)
