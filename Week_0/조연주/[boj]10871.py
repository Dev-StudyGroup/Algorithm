"""
X보다 작은 수
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=" ")