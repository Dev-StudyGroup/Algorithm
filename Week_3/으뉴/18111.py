import sys
from collections import Counter
input = sys.stdin.readline

n, m, b = map(int, input().split()) # n:세로, m:가로, b:블록개수
ground = []
for _ in range(n):
    ground += map(int, input().split())
height, time = 0, 1000000000000000

min_h = min(ground)
max_h = max(ground)
sum_h = sum(ground)
# ground 요소들의 각 개수를 딕셔너리 형태로 만듦
ground = dict(Counter(ground))

for i in range(min_h, max_h + 1): # 가장 낮은 높이 ~ 가장 높은 높이 
    if sum_h + b >= i * n * m: 
        cur_time = 0 # 현재 시간
        
        for key in ground: 
            if key > i: 
                cur_time += (key - i) * ground[key] * 2
            elif key < i:
                cur_time += (i - key) * ground[key]

        if cur_time <= time:
            time = cur_time
            height = i

print(time, height) 
            
                
