import sys
input = sys.stdin.readline
size = 10001
arr = [0] * size 
n = int(input()) 

for i in range(n): # n개 숫자 입력 받기
    tmp = int(input())
    arr[tmp] += 1 # n 인덱스에 1 추가
    
for i in range(size): # 배열 출력
    if arr[i] != 0: # 0이 아닌 요소를 출력
        for j in range(arr[i]): 
            print(i)
        

