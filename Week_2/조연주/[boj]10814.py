"""
나이순 정렬
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
n = int(input())
user = []

for i in range(n):
    age, name = input().split()
    user.append((int(age), name, i))

user.sort(key = lambda x :(x[0], x[2]))

for i in range(n):
    print(user[i][0], user[i][1])
