Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a=int(input())
b=int(input())
c=int(input())

result=list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))