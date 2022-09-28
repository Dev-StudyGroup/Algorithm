"""
단어 공부
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
from collections import Counter

c = Counter(input().upper())
most = c.most_common(2)

if len(most) > 1 and most[0][1] == most[1][1]:
    print('?')
else:
    print(most[0][0])
