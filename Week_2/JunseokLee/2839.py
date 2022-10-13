N = int(input())
result = 0
flag = False
while N % 5 != 0:
    N -= 3
    result += 1
    if N < 0:
        flag = True
        break
if flag:
    print(-1)
else:
    result += N//5
    print(result)