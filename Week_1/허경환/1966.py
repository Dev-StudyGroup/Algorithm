from collections import deque
#테스트케이스의 수 입력
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    ans=0
    target=m
    queue = deque(list(map(int, input().split())))
    while True:
        if target==0:
            now=queue.popleft()
            if len(queue)==0 or now >= max(queue):
                ans+=1
                break
            else:
                queue.append(now)
                target=len(queue)-1
        else:
            now = queue.popleft()
            target-=1
            if len(queue)==0 or now >= max(queue):
                ans+=1
            else:
                queue.append(now)
        
    print(ans)
