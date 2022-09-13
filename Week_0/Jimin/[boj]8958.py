'''
'OX퀴즈'
'''
t = int(input())
for i in range(t):
    answer = 0
    score = 0
    score_list = input()
    for j in score_list:
        if j == 'O':
            score += 1
        else:
            score = 0
        answer += score
    print(answer)