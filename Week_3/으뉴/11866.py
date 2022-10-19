import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(range(1, n+1))
ans = []
idx = 0

while arr:
    idx = (idx + k - 1) % len(arr) # 배열 크기에 따라 인덱스 변화
    ans.append(arr.pop(idx))
print('<'+', '.join(map(str, ans))+'>')
