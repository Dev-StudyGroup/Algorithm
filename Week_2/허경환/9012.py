#입력
t = int(input())

for _ in range(t):
    vps = input()
    stack = [0]
    for i in vps:
        if i=='(':
            stack.append('(')
        elif i==')':
            if stack[-1]=='(':
                stack=stack[:-1]
            else:
                stack.append(')')
                break
    if stack==[0]:
        print('YES')
    else:
        print('NO')
    
