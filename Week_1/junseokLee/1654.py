K, N = map(int, input().split())
lan = []
for k in range(K):
    lan.append(int(input()))

start, end = 1, max(lan)
result = 1
while start<=end:
    mid =(start+end)//2
    count = 0
    for i in range(len(lan)):
        count += lan[i]//mid
    if count < N:
        end = mid - 1
    elif count >= N:
        start = mid + 1
        result = mid

print(result)