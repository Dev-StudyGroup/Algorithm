'''
'스택 수열'
'''
import sys
input = sys.stdin.readline

n = int(input())
num_list = []       # 입력받을 수열
idx = 0             # num_list 탐색 idx
stack = []
answer = ''

for i in range(n):
    num = int(input())
    num_list.append(num)

end = 0
for i in range(1, n+1):
    stack.append(i)
    answer += '+'
    while True:
        if len(stack) == 0:
            break
        temp = stack[-1]
        if temp == num_list[idx]:
            idx += 1
            answer += '-'
            stack.pop()
        elif idx < n-1:
            if stack[-1] > num_list[idx]:
                end = 1
            break
    if end == 1:
        answer = 'NO'
        break

if answer == "NO":
    print(answer)
else:
    for i in answer:
        print(i)

