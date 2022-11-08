import sys

#입력
n = int(input())
ls = [sys.stdin.readline().strip() for i in range(n)]

#중복제거
ls=list(set(ls))

#사전순 정렬
ls.sort()

#길이순 정렬+출력
for i in range(1,51):
    for j in ls:
        if len(j)==i:
            print(j)
