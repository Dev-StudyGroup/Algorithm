n = int(input())
nums = map(int, input().split())
count = 0

for num in nums:
    notPrime = 0
    if num == 1: continue
    for i in range(2, num):
        if num % i == 0: 
            notPrime += 1
    if notPrime == 0: 
        count += 1

print(count)