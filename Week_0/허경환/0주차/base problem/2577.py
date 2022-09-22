#입력
a=int(input())
b=int(input())
c=int(input())

#카운트 결과를 저장할 배열
arr=[0]*10

#구현
result=str(a*b*c)
for i in result:
    arr[int(i)]+=1
#출력
for i in arr:
    print(i)


