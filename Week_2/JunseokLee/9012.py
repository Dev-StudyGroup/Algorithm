T = int(input())

for _ in range(T):
    s = input()
    flag = False
    cnt = 0
    for i in range(len(s)):
        if cnt < 0:
            flag = True
            break
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1
    if flag or cnt != 0:
        print("NO")
    else:
        print("YES")