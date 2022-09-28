'''
'제로'
'''
K = int(input())
stack = []
answer = 0
for i in range(K):
    n = int(input())
    if n == 0:
        num = stack.pop()
        answer -= num
    else:
        answer += n
        stack.append(n)
print(answer)