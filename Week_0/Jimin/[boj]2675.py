'''
'문자열 반복'
'''
T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    new_S = ''
    for i in S:
        new_S += i * R
    print(new_S)