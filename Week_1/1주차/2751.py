import sys
#입력
n = int(input())
num=[]
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

#정렬
num.sort()

#출력
for i in num:
    print(i)
