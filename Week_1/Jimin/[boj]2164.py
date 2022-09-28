'''
'카드2'
'''
N = int(input())

answer = 0
for i in range(1, N+1):
    if i == 1:
        answer = 1
    elif i == 2:
        answer = 2
    else:
        if answer + 2 > i:
            answer = 2
        else:
            answer += 2
print(answer)