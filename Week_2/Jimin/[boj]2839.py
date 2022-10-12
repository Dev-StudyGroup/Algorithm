'''
'설탕 배달'
'''
N = int(input())

d = [-1] * (N+1)
d[3] = 1

if N >= 4:
    d[4] = -1

if N >= 5:
    d[5] = 1

if N >= 6:
    for i in range(6, N+1):
        if d[i-3] == -1 and d[i-5] == -1:  
            d[i] = -1
        elif d[i-3] == -1:
            d[i] = d[i-5]+1
        elif d[i-5] == -1:
            d[i] = d[i-3]+1
        else:
            d[i] = min(d[i-3]+1, d[i-5]+1)

print(d[N])
