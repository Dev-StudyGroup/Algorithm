'''
프린터 큐

- 문제 요약
프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
    1. 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인
    2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치. 그렇지 않다면 바로 인쇄
현재 Queue에 있는 문서의 수와 중요도가 주어졌을때, 어떤 한 문서가 몇번째로 인쇄되는지 출력하는 프로그램

- 입력 조건
첫째 줄에 테스트케이스의 수가 주어짐. 각 테스트 케이스는 두 줄로 이루어짐.
테스트케이스의 첫번째 줄에는 문서의 개수 N(1 <= N <= 100)과 몇번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇번째에 놓여있는지를 나타내는 정수 M(0 <= M < N)이 주어짐.
이때 맨 왼쪽은 0번째라고 하자.
두번째 줄에는 N개 문서의 중요도가 차례대로 주어짐. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러개 있을 수 있다. 

- 출력 조건
각 테스트케이스에 대해 문서가 몇번째로 인쇄되는지 출력
'''
t = int(input())

def find_order(index,queue): # index: target이 어느 위치에 있는지
    order = 0
    while queue:
        if len(queue) > 1 and queue[0] < max(queue[1:]):
            temp = queue.pop(0)
            queue.append(temp)
            index -= 1
            if index == -1:
                index = len(queue) - 1
        
        else: # 맨 앞에 있는 문서보다 중요도가 높은 문서가 없을 때
            queue.pop(0)
            order += 1
            if index == 0:
                break
            else:
                index -= 1
    
    return order

for _ in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    print(find_order(m, importance))
