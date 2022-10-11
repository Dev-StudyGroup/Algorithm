'''
블랙잭

- 문제 요약
각 카드에는 양의 정수가 쓰여있다.
N장의 카드가 주어졌을때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하는 프로그램.

- 입력 조건
첫째 줄에 카드의 개수 N(3 <= N <= 100)과 M(10 <= M <= 300,000)이 주어진다. 
둘째 줄에는 카드에 쓰여있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다. 

- 출력 조건
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
'''
from itertools import combinations
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0
combi = list(combinations(card, 3))
for i in combi:
    if result <= sum(i) <= m:
        result = sum(i)
print(result)
