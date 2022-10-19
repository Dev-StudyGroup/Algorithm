"""
11866: 요세푸스 문제
"""
n, k = map(int, input().split())

dq = [i for i in range(1, n+1)]
ans = []
idx = k-1
while len(dq) > 0:
    if idx >= len(dq):
        while idx >= len(dq):
            idx -= len(dq)
    ans.append(dq.pop(idx))
    idx += k-1

print("<", end="")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end=">")
    else: print(ans[i], end=", ")

