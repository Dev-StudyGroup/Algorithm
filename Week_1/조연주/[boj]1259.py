"""
팰린드롬수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
while 1:
    t = list(input())
    if t == ['0']:
        break
    else:
        reverse_t = list(reversed(t))

        if t == reverse_t:
            print('yes')
        else:
            print('no')
