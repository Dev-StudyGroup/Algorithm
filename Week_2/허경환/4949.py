answer=[]

while True:
    #입력
    string = input()
    if string == '.':
        break
    #스택
    stack = []
    #플래그
    flag=True
    
    #문자열을 한 글자씩 반복
    for i in string:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)==0:
                answer.append('no')
                flag=False
                break
            tmp=stack.pop()
            if tmp!='(':
                answer.append('no')
                flag=False
                break
        
        elif i==']':
            if len(stack)==0:
                answer.append('no')
                flag=False
                break
            tmp=stack.pop()
            if tmp!='[':
                answer.append('no')
                flag=False
                break
        elif i=='.':
            if len(stack)!=0:
                answer.append('no')
                flag=False
    
    if flag==True:
        answer.append('yes')
    

for i in range(len(answer)):
    print(answer[i])
