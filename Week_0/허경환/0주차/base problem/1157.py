#입력
word = input().upper()

alpha=[0]*26
for i in word:
    alpha[ord(i)-ord('A')]+=1

m_num=max(alpha)

count=0
for i in alpha:
    if i==m_num:
        count+=1

if count>1:
    print("?")
elif count==1:
    print(chr(alpha.index(m_num)+ord('A')))
