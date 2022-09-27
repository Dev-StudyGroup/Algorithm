"""
제로
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop(-1)
    else:
        stack.append(n)
    
print(sum(stack))
