from collections import deque
import sys


#큐
queue = deque([])

#push
def push(x):
    queue.append(x)
    
#pop
def pop():
    if len(queue)==0:
        print(-1)
    else:
        num=queue.popleft()
        print(num)
    
#size
def size():
    print(len(queue))
    
#empty
def empty():
    if len(queue)==0:
        print(1)
    else:
        print(0)
        
#front
def front():
    if len(queue)==0:
        print(-1)
    else:
        print(queue[0])

#back
def back():
    if len(queue)==0:
        print(-1)
    else:
        print(queue[-1])



#입력
n = int(input())
for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd=='front':
        front()
    elif cmd=='back':
        back()
    elif cmd=='empty':
        empty()
    elif cmd=='size':
        size()
    elif cmd=='pop':
        pop()
    else:
        ls=list(cmd.split())
        push(ls[1])
