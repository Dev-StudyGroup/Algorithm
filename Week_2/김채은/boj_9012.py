n = int(input())

answer = []

for _ in range(n):
    
    ps = input()

    if ps == '.':
        break

    stack = []

    for s in ps:
        if s in '(':
            stack.append(s)
        elif s in ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break

    if stack:
        answer.append("NO")
    else:
        answer.append("YES")

for a in answer:
    print(a)
    