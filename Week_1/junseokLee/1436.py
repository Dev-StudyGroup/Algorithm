N = int(input())
count = 0
num = 665
result = 666
while True:
    num += 1
    n = str(num)
    if n.count("666")>=1:
        count += 1
    if count == N:
        result = n
        break
print(result)