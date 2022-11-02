import sys
#입력
n = int(sys.stdin.readline().strip())
member=[]
for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    member.append((int(age),name))

#정렬
member.sort(key=lambda x : x[0])

#출력
for i,j in member:
    print(i, end=' ')
    print(j)
