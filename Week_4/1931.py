"""
1931: 회의식 배정
"""
import sys

n = int(sys.stdin.readline())
time = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

start = time[0][1] 
count = 1

for i in range(1, n): 
    if start <= time[i][0]: # 앞 타임의 끝나는 시간이 뒷 타임의 시작하는 시간보다 이르면
        count += 1
        start = time[i][1]

print(count)
        
