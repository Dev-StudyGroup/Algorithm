'''
'블랙잭'
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
answer = 0

for i in range(len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            total = card[i] + card[j] + card[k]
            if total <= M:
                answer = max(answer, total)

print(answer)