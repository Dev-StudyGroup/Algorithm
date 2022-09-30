Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
word=input().upper()

words=list(set(word))
cntList=[]

for i in words:
    cnt = word.count(i)
    cntList.append(cnt)

    
if cntList.count(max(cntList))>1:
    print(?)
    
SyntaxError: invalid syntax
if cntList.count(max(cntList))>1:
    print('?')
else :
    index=cntList.index(max(cntList))
    print(words[index])