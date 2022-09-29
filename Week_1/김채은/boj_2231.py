n = int(input())

answer = 0

for i in range(n, 0, -1):
    temp = i
    _sum = i
    while temp > 0:
        _sum += temp % 10
        temp //= 10

    if _sum == n:
        answer = i
    
print(answer) 
