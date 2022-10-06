result = []
n = int(input())

for _ in range(n):
    string = input()
    open_cnt, close_cnt = 0, 0
    flag = True

    for s in string:
        if s == '(':
            open_cnt += 1
        elif s == ')':
            close_cnt += 1
        
        if close_cnt > open_cnt:
            flag = False
            break

    if close_cnt != open_cnt:
        flag = False
    
    if flag:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)