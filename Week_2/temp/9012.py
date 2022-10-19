"""
9012: 괄호
"""

t = int(input())
for i in range(t):
    vps = input()
    stack = []; flag = True
    for i in vps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                flag = False
                break
            elif stack[-1] == "(":
                stack.pop()
    if flag == True and not stack:
        print("YES")
    else:
        print("NO")
