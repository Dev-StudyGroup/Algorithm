from collections import deque

#입력
n, k = map(int, input().split())
ls = [i for i in range(1, n+1)]
queue=deque(ls)

ans=[]
while queue:
    queue.rotate(-k+1)
    ans.append(queue.popleft())

#출력
print('<', end='')
for i in ans[:-1]:
    print(str(i)+', ', end='')
print(str(ans[-1]), end='')
print('>')
