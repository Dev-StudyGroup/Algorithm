#입력
ls=[]
for i in range(10):
    ls.append(int(input())%42)
    
#중복제거
ls=list(set(ls))
#출력
print(len(ls))
