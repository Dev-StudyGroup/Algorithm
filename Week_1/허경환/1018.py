import sys
#입력
n, m = map(int, sys.stdin.readline().split())
matrix=[[] for _ in range(n)]
for i in range(n):
    matrix[i]=list(sys.stdin.readline())


#맨 왼쪽 위 칸이 흰색인 경우, 칠해야할 칸 수를 계산하는 함수
def w_count(i, j):
    result=0
    for k in range(8):
        for l in range(8):
            if (k+l)%2==0 and matrix[i+k][j+l]=='B':
                result+=1
            if (k+l)%2==1 and matrix[i+k][j+l]=='W':
                result+=1   
    return result


#맨 왼쪽 위 칸이 검은색인 경우, 칠해야하는 칸 수를 계산하는 함수
def b_count(i, j):
    result=0
    for k in range(8):
        for l in range(8):
            if (k+l)%2==0 and matrix[i+k][j+l]=='W':
                result+=1
            if (k+l)%2==1 and matrix[i+k][j+l]=='B':
                result+=1   
    return result


#8*8크기 체스판 추출 후 계산
answer=n*m
for i in range(n-7):
    for j in range(m-7):
        count=min(w_count(i,j), b_count(i,j))
        if answer>count:
            answer=count
#출력
print(answer)
