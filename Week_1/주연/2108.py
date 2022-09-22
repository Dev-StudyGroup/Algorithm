n = int(input())
arr = [int(input()) for _ in range(n)]
#산술평균
print(round(sum(arr)/n))
arr.sort()
#중앙값
print(arr[int((n-1)/2)])
#최빈값
cnts = dict()
for i in range(1, n+1):
    cnts[i] = []
print(cnts)

maxCnt = 1
cnt = 1
for i in range(1,n):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnts[cnt].append(arr[i-1])
        if maxCnt < cnt: maxCnt = cnt
        cnt = 1
    if i == n-1:
        cnts[cnt].append(arr[i])
        if maxCnt < cnt: maxCnt = cnt
if n == 1: cnts[1].append(arr[0])
cnts[maxCnt].sort()
print("cnts", cnts)
if len(cnts[maxCnt]) == 1: print(cnts[maxCnt][0])
else: print(cnts[maxCnt][1])

#범위
print(arr[-1]-arr[0])