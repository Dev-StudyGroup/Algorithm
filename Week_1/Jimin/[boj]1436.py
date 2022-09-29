'''
'영화감독 숌'
'''
N = int(input())

order = 0
num = 666
while True:
    if '666' in str(num):
        order += 1
        if order == N:
            break
    num += 1

print(num)