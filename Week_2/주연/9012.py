n = int(input())
for i in range(n):
    val = list(input())
    sum = 0
    for x in val:
        if x =='(': sum+=1
        else: sum-=1
        if sum < 0:
            sum = -1
            break
    if sum == 0: print('YES')
    else: print('NO')