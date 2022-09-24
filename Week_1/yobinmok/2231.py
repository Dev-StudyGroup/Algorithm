# ver 1 : 길이는 짧지만 시간은 긺
n = int(input())
nums = []; s = 0
for i in range(n):
    s = i; i = str(i)
    for j in range(len(i)):
        s += int(i[j]) # 분해합 구함
    if s == n:
        answer = i
        break;
    else:
        answer = 0
print(answer)