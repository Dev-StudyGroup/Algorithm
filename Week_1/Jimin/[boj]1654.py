'''
'랜선 자르기'
'''
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
string = []
for i in range(K):
    num = int(input())
    string.append(num)

end = max(string)
start = 1

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in string:
        cnt += i // mid
    if cnt < N:
        end = mid - 1
    elif cnt >= N:
        start = mid + 1

print(end)