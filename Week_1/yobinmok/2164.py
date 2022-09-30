# 시간초과 해결
# 해당 로직은 큐처럼 동작하지만 리스트로 구현했기에 값을 넣고 빼는 과정에서 성능이 저하됨
# 큐를 사용하여 문제 해결

import sys
from collections import deque

n = int(sys.stdin.readline())
cards = [x for x in range(1, n+1)] # 배열 초기화 방법!
cards = deque(cards)

while len(cards) > 1:
    cards.popleft() # 홀수번 째 카드 버리기
    cards.append(cards.popleft()) # 짝수번 째 카드 맨 아래에 넣기

print(cards[0])
