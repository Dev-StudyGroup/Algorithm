def is_balanced():
    global flag
    for s in str:
        if s == '[' or s == '(':
            stack.append(s)
        if s == ']':
            if len(stack) == 0:
                flag = True
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
        if s == ')':
            if len(stack) == 0:
                flag = True
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break

while True:
    str = input().rstrip()
    stack = []
    flag = False

    if len(str) == 1 and str[0] == '.':
        break

    is_balanced()

    if len(stack) == 0 and not flag:
        print("yes")
    else:
        print("no")
