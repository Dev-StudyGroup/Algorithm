"""
벌집
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())
start = 1
cnt = 1

while n > start :
    start += 6 * cnt
    cnt += 1
print(cnt)