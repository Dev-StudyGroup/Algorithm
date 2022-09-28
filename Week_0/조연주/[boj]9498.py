"""
시험 성적
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())

if n >= 90 and n <= 100:
    print('A')
elif n >= 80 and n < 90:
    print('B')
elif n >= 70 and n < 80:
    print('C')
elif n >= 60 and n < 70:
    print('D')
else:
    print('F')
