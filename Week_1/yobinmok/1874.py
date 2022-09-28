n = int(input())

stack = []
answers = []
flag = 0
j = 1
for i in range(n):
    num = int(input())
    while j <= num:
        stack.append(j)
        answers.append("+")
        j += 1
    if stack[-1] == num:
        stack.pop()
        answers.append('-')
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for answer in answers:
        print(answer)