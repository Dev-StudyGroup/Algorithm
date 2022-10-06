#입력
n = int(input())
ls=[]
for _ in range(n):
    ls.append(int(input()))
    
# + - 저장 리스트
ans=[]
#스택
stack=[-1]

#구현
count=1
flag=False
for i in ls:
    while True:
        if stack[-1]!=i:
            stack.append(count)
            ans.append('+')
            count+=1
        else:
            stack=stack[:-1]
            ans.append('-')
            break
            
        if count>n+1:
            print('NO')
            flag=True
            break
    if flag==True:
        break

#출력
if flag==False:
    for i in ans:
        print(i)

