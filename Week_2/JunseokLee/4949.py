while True:
    s = input()
    small = 0
    large = 0
    last = []
    flag = False
    if len(s) == 1 and s[0] == '.':
        break
    for i in range(len(s)):
        if small < 0 or large < 0:
            flag = True
            break
        if s[i] == '(':
            small += 1
            last.append('(')
        elif s[i] == ')':
            small -= 1
            if len(last)>0 and last[len(last)-1]!='(':
                flag = True
                break
            elif len(last)>0 and last[len(last)-1]=='(':
                last.pop()
        elif s[i] == '[':
            large += 1
            last.append('[')
        elif s[i] == ']':
            large -= 1
            if len(last)>0 and last[len(last)-1]!='[':
                flag = True
                break
            elif len(last) > 0 and last[len(last) - 1] == '[':
                last.pop()
    if small != 0 or large != 0:
        flag = True
    if flag:
        print("no")
    else:
        print("yes")
