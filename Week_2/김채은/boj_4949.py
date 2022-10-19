answer = []
while True:
    string = input()

    if string == '.':
        break

    stack = []

    for s in string:
        if s in ['[', '(']:
            stack.append(s)
        elif s in [']', ')']:
            if stack and (stack[-1], s) in [('[', ']'), ('(', ')')]:
                stack.pop()
            else:
                stack.append(s)
                break

    if stack:
        answer.append("no")
    else:
        answer.append("yes")

for a in answer:
    print(a)