'''
'알람 시계'
'''
H, M = map(int, input().split())
if M < 45:
    M = 60 - (45-M)
    H -= 1
else:
    M -= 45

if H < 0:
    H = 23

print(H, M)