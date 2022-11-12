from collections import deque

#입력
n = int(input())
card=deque([])
for i in range(1, n+1):
    card.append(i)
    
#구현
while True:
    if len(card)==1:
        print(card[0])
        break
    card.popleft()
    top=card.popleft()
    card.append(top)


