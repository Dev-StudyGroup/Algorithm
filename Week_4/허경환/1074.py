#입력
n, r, c = map(int, input().split())

#방문한 칸 개수
count=-1



#분할정복 구현
def div_con(n, r, c):
    global count
    if n==0:
        count+=1
    else:
        if r<(2**n//2) and c<(2**n//2): #1
            div_con(n-1, r, c)
        elif r<(2**n//2) and c>=(2**n//2): #2
            count+=((2**n//2)**2)
            div_con(n-1, r, c-(2**n//2))
        elif r>=(2**n//2) and c<(2**n//2): #3
            count+=((2**n//2)**2)*2
            div_con(n-1, r-(2**n//2), c)
        elif r>=(2**n//2) and c>=(2**n//2): #4
            count+=((2**n//2)**2)*3
            div_con(n-1, r-(2**n//2), c-(2**n//2))
        
#분할정복 실행
div_con(n, r, c)

#출력
print(count)


