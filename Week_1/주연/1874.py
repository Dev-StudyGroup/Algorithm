n = int(input())

flag = 0
cnt = 0
stack = []
answer = []

for i in range(n):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        answer.append('+')

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)