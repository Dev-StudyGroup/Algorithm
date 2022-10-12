result = []
while 1:
    string = input()
    if string == '.':
        break

    flag, temp = True, []
    for s in string:
        if s == '[' or s == '(':
            temp.append(s)
        elif s == ']':
            if not temp or temp[-1] == '(':
                flag = False
                break
            elif temp[-1] == '[':
                temp.pop()
        elif s == ')':
            if not temp or temp[-1] == '[':
                flag = False
                break
            elif temp[-1] == '(':
                temp.pop()

    if flag and not temp:
        result.append('yes')
    else:
        result.append('no')

for r in result:
    print(r)