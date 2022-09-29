"""

    stack에 push하는 순서는 반드시 오름차순을 지키도록하자

    push 조건::
        1. stack[-1] < push하는 number
        안될 시 NO
    stack, sequence가 같을 때, 출력
    1, 2, 3, 4, 5, 6, 7, 8
    i <= index

    1, 2, 5, 7, 8, 6, 3, 4,
    j <= index


"""

n = int(input())
result = []
stack = []
find = True
now = 1
for _ in range(0, n):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        find = False

if not find:
    print('NO')
else:
    for i in result:
        print(i)




