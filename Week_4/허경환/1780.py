#입력
n = int(input())
arr=[[] for i in range(n)]
for i in range(n):
    arr[i]=list(map(int, input().split()))

    
#문제유형 -> 최적부분구조=큰문제와 작은문제의 구조가 같음, 작은문제가 중복되지 않음
#분할정복

#-1,0,1 종이개수
num_m_one = 0
num_zero = 0
num_one = 0

#종이가 모두 같은 수로 되어 있는지 확인하는 함수
def div_con(n, arr, x0, y0):
    global num_m_one
    global num_zero
    global num_one
    
    #종이 안의 수가 모두 같은지 확인하기
    num=arr[x0][y0]
    flag=True
    for i in range(x0, x0+n):
        for j in range(y0, y0+n):
            if arr[i][j]!=num:
                flag=False
                break
        if flag==False:
            break
    
    #만약 종이의 수가 모두 같다면
    if flag==True:
        if num==-1:
            num_m_one+=1
        elif num==0:
            num_zero+=1
        elif num==1:
            num_one+=1
    
    #만약 종이의 수가 모두 같지 않다면
    else:
        for i in range(3):
            for j in range(3):
                div_con(n//3, arr, x0+i*(n//3), y0+j*(n//3))
        

#분할정복 실행
div_con(n, arr, 0, 0)

#출력
print(num_m_one)
print(num_zero)
print(num_one)
