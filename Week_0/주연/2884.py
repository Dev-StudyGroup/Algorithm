Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
h,m= input().split()
if int(h) != 0:
    if int(m)<45:
        print(int(h)-1,int(m)+15)
    else:
        print(int(h), int(m)-45)
else :
    if int(m)<45:
        print(23,int(m)+15)
    else:
        print(int(h), int(m)-45)