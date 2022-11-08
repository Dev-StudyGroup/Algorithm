#입력
s = input()
ls=[]
num=''
for i in s:
    if i=='-' or i=='+':
        ls.append(int(num))
        num=''
        ls.append(i)
    else:
        num+=i
if num!='':
    ls.append(int(num))

#그리디알고리즘
# - num + 꼴이면 num앞에서 괄호열고, + num - 꼴이거나 + num 꼴일 때 num뒤에서 괄호 닫기.
#정당성 검토 : - 연산자 뒤에 +로 연결된 num들을 모두 더한 다음에 빼는 게 항상 가장 작은 수이다.

#구현
plus=0
minus=0
flag=True
for i in range(len(ls)):
    if ls[i]=='+':
        continue
    if ls[i]!='-':
        if flag==True:
            plus+=ls[i]
        else:
            minus+=ls[i]
    elif ls[i]=='-':
        flag=False
#출력
print(plus-minus)
