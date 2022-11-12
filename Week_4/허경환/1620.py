#입력
n, m = map(int, input().split())

pocketmon={}
for i in range(1,n+1):
    pocketmon[i]=input()

reverse_pocketmon=dict(map(reversed, pocketmon.items()))
    
problem=[0]
for i in range(m):
    problem.append(input())

#출력
for i in problem[1:]:
    #숫자면
    if i.isdigit():
        print(pocketmon[int(i)])
    
    #문자면
    if i.isalpha():
        print(reverse_pocketmon[i])
