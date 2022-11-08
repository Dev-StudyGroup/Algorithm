'''
카드2

- 문제 요약
1부터 N까지의 번호가 있는 N장의 카드. 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여있다.
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복. 
    우선, 제일 위에 있는 카드를 바닥에 버린다. 
    그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
ex) N=4
    1234 -> (1버림)234 -> (2밑으로)342 -> (3버림)42 -> (4밑으로)24 -> (2버림)4
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램.

- 입력 조건
첫째 줄에 정수 N(1<= N <= 500,000)이 주어짐

- 출력 조건
첫째 줄에 남게 되는 카드의 번호 출력.
'''
from collections import deque

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while True:
    head = queue.popleft() # 제일 위 카드 버림
    if not queue:
        break
    head = queue.popleft()
    if not queue:
        break
    queue.append(head)
print(head)
