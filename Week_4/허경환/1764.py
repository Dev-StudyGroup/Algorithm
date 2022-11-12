#입력
n, m = map(int, input().split())
no_hear=set()
no_see=set()
for i in range(n):
    no_hear.add(input())
for i in range(m):
    no_see.add(input())
    
#교집합
no_see_hear=no_hear & no_see

#리스트로 변경
ls = list(no_see_hear)
ls.sort()

#출력
print(len(ls))
for i in ls:
    print(i)



