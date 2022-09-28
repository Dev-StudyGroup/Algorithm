#입력
s = input()
alpha=[-1]*26
count=-1
for i in s:
    count+=1
    if alpha[ord(i)-ord('a')]==-1:
        alpha[ord(i)-ord('a')]=count

#출력
for i in alpha:
    print(i, end=' ')
