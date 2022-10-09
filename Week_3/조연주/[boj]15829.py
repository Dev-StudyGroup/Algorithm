"""
Hashing
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
l = int(input())
string = input()
value = 0

for i in range(l):
    value += (ord(string[i]) - 96) * (31 ** i)

print(value)
