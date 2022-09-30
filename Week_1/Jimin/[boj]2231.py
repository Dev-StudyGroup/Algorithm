'''
'분해합'
'''
N = int(input())

for i in range(N//2, N):
    strI = str(i)
    num = i
    for j in strI:
        num += int(j)
    if num == N:
        print(i)
        break
    num = 0

if num == 0:
    print(0)