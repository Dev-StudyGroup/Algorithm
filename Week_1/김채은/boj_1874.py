# [BOJ] 1874 스택 수열
# Time Taken: 1h 30m

answer = []

n = int(input())
arr = [int(input()) for _ in range(n)]

index = 0
num = 1

stack = []

while True:
    if not stack or stack[-1] != arr[index]:
        if num <= n:
            stack.append(num)
            answer.append('+')
            num += 1
        else:
            break
    else:
        stack.pop()
        answer.append('-')
        index += 1

    if index==n:
        break

if index==n:
    for a in answer:
        print(a)
else:
    print('NO')
