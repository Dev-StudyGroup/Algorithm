n = int(input())
cur_num = 1
point = 0
stack = []
answer = []
flag = True

for i in range(n):
    num = int(input())
    while cur_num <= num:
        stack.append(cur_num)
        answer.append('+')
        cur_num += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = False
        break
if flag:
    for i in answer:
        print(i)
