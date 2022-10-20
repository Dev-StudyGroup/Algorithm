T = int(input())

def check_VPS():
    global flag
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) == 0:
                flag = True
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break


for _ in range(T):
    str = input().rstrip()
    stack = []
    flag = False

    check_VPS()

    if len(stack) == 0 and not flag:
        print("YES")
    else:
        print("NO")
