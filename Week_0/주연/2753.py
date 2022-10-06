Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
year=int(input())
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
    print(1)
else:
    print(0)