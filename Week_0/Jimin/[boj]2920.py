'''
'음계'
'''
music = list(map(int, input().split()))
answer = ''
if music[0] == 1:
    now = 1
    answer = 'ascending'
    for i in music:
        if i != now:
            answer = 'mixed'
        now += 1
elif music[0] == 8:
    now = 8
    answer = 'descending'
    for i in music:
        if i != now:
            answer = 'mixed'
        now -= 1
else:
    answer = 'mixed'

print(answer)