import sys

#스택
stack = []

#push
def push(x):
    stack.append(x)
#pop
def pop():
    if stack==[]:
        print(-1)
    else:
        num=stack.pop()
        print(num)
    
#size
def size():
    print(len(stack))
    
#empty
def empty():
    if stack==[]:
        print(1)
    else:
        print(0)
        
#top
def top():
    if stack==[]:
        print(-1)
    else:
        print(stack[-1])




#입력
n = int(input())
for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd=='top':
        top()
    elif cmd=='empty':
        empty()
    elif cmd=='size':
        size()
    elif cmd=='pop':
        pop()
    else:
        ls=list(cmd.split())
        push(ls[1])
