from collections import deque
import sys


#덱
deq = deque([])

#push_front
def push_front(x):
    deq.appendleft(x)

#push_back
def push_back(x):
    deq.append(x)

#pop_front
def pop_front():
    if len(deq)==0:
        print(-1)
    else:
        num=deq.popleft()
        print(num)

#pop_back
def pop_back():
    if len(deq)==0:
        print(-1)
    else:
        num=deq.pop()
        print(num)        
        
#size
def size():
    print(len(deq))
    
#empty
def empty():
    if len(deq)==0:
        print(1)
    else:
        print(0)
        
#front
def front():
    if len(deq)==0:
        print(-1)
    else:
        print(deq[0])

#back
def back():
    if len(deq)==0:
        print(-1)
    else:
        print(deq[-1])



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
    elif cmd=='pop_front':
        pop_front()
    elif cmd=='pop_back':
        pop_back()
    else:
        ls=list(cmd.split())
        if ls[0]=='push_front':
            push_front(ls[1])
            
        elif ls[0]=='push_back':
            push_back(ls[1])
            
