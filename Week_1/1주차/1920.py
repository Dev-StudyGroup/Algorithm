#입력
n = int(input())
arr=list(map(int, input().split()))
m = int(input())
num=list(map(int, input().split()))

#집합으로 변환
set_arr=set(arr)

#set_arr집합안에 m개의 수들이 각각 존재하는지 확인
for i in num:
    if i in set_arr:
        print(1)
    else:
        print(0)
