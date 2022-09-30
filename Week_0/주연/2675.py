Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
caseNum=int(input())

for i in range(caseNum):
    r,s=input().split()
    text=''
    for i in s:
        text+=int(r)*i
    print(text)